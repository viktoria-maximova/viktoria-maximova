# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list = []
element_count = int (input('Введите количество элементов списка: '))
i = 1
while i <= element_count:
    list.append(input('Введите значение элемента списка: '))
    i += 1
print(list)

len_list = len(list)
element = 0
while element < len_list - 1:
        list[element], list[element + 1] = list[element + 1], list[element]
        element += 2
print(list)



