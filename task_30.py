""" Пам-парам парам-пам парам """

text = input('Пишите стих: ')


def check(text):
    sets = set()
    for i in text.split():
        count = 0
        for j in i:
            if j in 'аиоуыэеёюя':
                count += 1
        sets.add(count)
    if len(sets) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'


print(check(text))
