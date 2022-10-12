seconds = int(input('Введите время в секундах: '))
seconds %= 86400
hour = seconds // 3600
seconds %= 3600
minute = seconds // 60
seconds %= 60
print('%d:%d:%d' % (hour, minute, seconds))