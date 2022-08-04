""" Все равны, как на подбор """


values = [0, 2, 10, 6]


def same_by(characteristic, objects):
    return len(set(map(characteristic, values))) == 1 if values else True


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
