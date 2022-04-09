# 2. Пconds:02}")ользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
s = int(input("Введите время в секундах: "))
#print(s)
#time  = h, m, s
m = int (s / 60)
#print (m)
h = int (s / 3600)
#print (h)
# hh:mm:ss 3600 сек -1 час 00 мин и 00 сек -print 120 сек это 00ч 2 мин 00сек, 30сек -это 00 час, 00 мин, 30 сек
# форматирование строк
if (s>=0 and s<=59):
    print ('{} : {} : {}'.format(h,m, s))
elif (s>=60 and s<=3600):
    n = s - m * 60
    print('{} : {} : {}'.format(h, m, n))
elif (s>3600):
    # 3723 1  час 2 мин 3 сек 3723 - 1 час * 60 3723-3600 123
    l = int((s - h * 3600) / 60)
    k = int(s - h * 3600 - l * 60)
    print('{} : {} : {}'.format(h, l, k ))

#time = int(input("Enter the time in seconds: "))
#time = int(input("Enter the time in seconds: "))
#hours = time // 3600
#minutes = time // 60 - hours * 60
#seconds = time % 60
#print(f"{hours:02}:{minutes:02}:{seconds:02}")


