# Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

print('Таблица умножения')
 
for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
else:
    print('Its off')