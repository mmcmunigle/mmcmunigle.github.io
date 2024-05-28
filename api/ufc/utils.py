def correct_name(name):
    name_corrections = {
        'Sergey Pavlovich': 'Sergei Pavlovich',
        'Elves Brenner': 'Elves Brener',
        'José Aldo': 'Jose Aldo',
        'Paulo Henrique Costa': 'Paulo Costa',
        'Khaos Williams': 'Kalinn Williams',
        'Tuco Tokkos': 'George Tokkos',
        'Alatengheili': 'Heili Alateng',
        'Kleydson Rodrigues': 'Kleidiso Rodrigues',
        'Alexander Romanov': 'Alexandr Romanov',
        'Elizeu Zaleski dos Santos': 'Elizeu Zaleski Dos Santos',
        'Phil Rowe': 'Philip Rowe',
    }

    name = name.replace('é', 'e').replace('ł', 'l').replace('á', 'a').replace('Ľ', 'L')
    if name in name_corrections:
        return name_corrections[name]
    else:
        return name