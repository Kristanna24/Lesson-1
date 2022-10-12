n = (input('Введите число: '))
a = n
b = n + n
c = n + n + n
result = ('%s + %s + %s' % (a, b, c))
print(result, '=', int(a[:]) + int(b[:]) + int(c[:]))