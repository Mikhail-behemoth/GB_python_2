# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если 
# ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    cities = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        cities[v] = k
    return cities

print(hashable_dicts(Russia='Moscow', Turkey={'Ankara': 2, 'Istanbul': 3}, China=['Shanghai', 'Peking'], Australia={'Canberra', 'Sydney'}))