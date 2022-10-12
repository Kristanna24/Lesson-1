count = int(input('Введите целое, положительное число: '))
number = 0
while count > 0:
    number = max(number, count % 10)
    count //= 10
print(number)