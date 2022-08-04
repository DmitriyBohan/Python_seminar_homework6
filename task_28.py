""" Мимикрия """
values = [1, 23, 42, 'asdfg']
transformation = lambda z:z


transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')

