import csv
from threading import Thread

import requests


class UFCMerchandise:
    def __init__(self):
        self.merchandise_url = "https://marketplace.draftkings.com/fetcher/8b8f14fb451944aca580a1e6bcb95cd4/merchandise?offset=0&limit=50000&orderByType=ListDate&collectionKey=8b8f14fb451944aca580a1e6bcb95cd4&isDescending=true&resultType=Collectible&rangeFilterValuesByAttributeId=%7B%7D&_data=routes%2F__main%2Ffetcher%2F%24collectionKey%2Fmerchandise"
        self.merchandise = {}

    def update_merchandise(self):
        response = requests.get(self.merchandise_url)
        if response.ok:
            self.merchandise = process_cards(response.json()['merchandise'])
        else:
            print(f"Error getting merchandise: {response.text}")
        
        print("Successfully Updated Market Data")


def process_cards(cards):
    """process a all merchandice cards"""
    merchandise = {}
    for card in cards:
        attributes = parse_attributes(card)

        name = attributes['athlete_name']
        if name not in merchandise:
            merchandise[name] = {
                'core': {},
                'rare': {},
                'elite': {},
                'legendary': {},
                'reignmaker': {}
            }
        
        rarity = attributes.get('rarity_tier').lower()
        set_name = attributes.get('set_name')
        link = f"https://marketplace.draftkings.com/listings/collectibles/{card['merchandiseKey']}/"

        if not set_name in  merchandise[name][rarity].keys():
             merchandise[name][rarity][set_name] = {}

        merchandise[name][rarity][set_name] = {
            'price': round(card['lowestListedEditionPrice'], 2),
            'quantity': card['quantity'],
            'link': link,
            'division': attributes.get('division'),
            'champion': attributes.get('champion_status'),
            'edition_tier': attributes.get('edition_tier'),
        }

    return merchandise


def parse_attributes(content):
    attributes = {}
    for attribute in content['collectionAttributes']:
        name = attribute['displayName'].replace(' ', '_').lower()
        attributes[name] = attribute['value']

    return attributes
