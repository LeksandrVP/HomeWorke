"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

try:
    month = int(input("Введите номер месяца чисом: "))
except ValueError:
    print("Неверно ввели номер месяца")
else:
    Summer = [6, 7, 8]
    Winter = [12, 1, 2]
    Spring = [3, 4, 5,]
    Autumn = [9, 10, 11]
    if month in Summer:
        print('Лето')
    elif month in Winter:
        print('Зима')
    elif month in Spring:
        print('Весна')
    elif month in Autumn:
        print('Осень')