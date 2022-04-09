#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


#n = input("Enter an integer: ")
#while n < '0':
#   print("I've asked for number greater than 0! Please try again!")
#  n = input('Please enter number greater than 0: ')
#print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

n = input('Введите целое положительное число: ')
#print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
print(n)
a = n + n
print (a)
b = n+n+n
print(b)
print(int(n) + int(a) + int(b))
