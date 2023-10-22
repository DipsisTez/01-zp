from itertools import permutations

def sort_dict(x):
    return dict((k, ''.join(sorted(v))) for k, v in sorted(x.items()))

def map_values(x, c):
    return {c[k]: ''.join(c[d] for d in v) for k, v in x.items()}

# Исходные данные
s = {'1': '24', '2': '146', '3': '56', '4': '1267', '5': '36', '6': '23457', '7': '46'}
S = sort_dict({'А': 'БВ', 'Б': 'АВ', 'В': 'АБДЕГ', 'Г': 'ВЕК', 'Д': 'ВЕ', 'Е': 'ДВГК', 'К': 'ЕГ'})

# Получение номеров городов
for i in permutations('1234567'):
    t = {k: v for k, v in zip(i, 'АБВГДЕК')}
    if sort_dict(map_values(s,t)) == S:
        print(t)
        break
