#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input ('Введите число: ')
print (n)

nn = f'{n}{n}'
print (nn)

nnn = f'{n}{n}{n}'
print (nnn)

result = int (n) + int (nn) + int (nnn)
print(result)
