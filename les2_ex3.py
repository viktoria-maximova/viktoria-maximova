# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.


#вариант со списком:
num_month = int (input('Введите месяц в виде целого числа от 1 до 12: '))
list = [0,12,1,2,3,4,5,6,7,8,9,10,11]

if num_month in list[1:4]:
    print('зима')
elif num_month in list[4:7]:
    print('весна')
elif num_month in list[7:10]:
    print('лето')
else:
    print('осень')

#вариант со словарем:
num_month = int (input('Введите месяц в виде целого числа от 1 до 12: '))
dict = {'зима': [12,1,2], 'весна':[3,4,5], 'лето':[6,7,8],'осень':[9,10,11]}
for key, value in dict.items():
    if num_month in value:
        print(key)