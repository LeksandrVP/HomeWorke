"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

input_list = input("Введите через пробел элементы списка: ")
input_list = input_list.split(" ")

for index in range(0, len(input_list)-2, 4):
    input_list[index], input_list[index+1] = input_list[index+1], input_list[index]

print(input_list)