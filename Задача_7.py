first = int(input('Введите расстояние первой пробежки спортсмена в км.: '))
result = int(input('Введите необходимый результат в км.: '))
day = 1
while result > first:
    day += 1
    first *= 1.1
    print(f' {day}-й день: ', '{0:4.2f} км'.format(first))
print(f'На {day} день спортстмен достиг результата - не менее {result} км.')