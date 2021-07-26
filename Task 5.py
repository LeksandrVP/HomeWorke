"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

rating_list = [9, 6, 3, 2, 1]
rating_list_copy = rating_list.copy()
new_rating = int(input("Введите новый элемент рейтинга:"))
if new_rating > rating_list[0]:
    rating_list_copy.incert(0, new_rating)
elif new_rating < rating_list[-1]:
    rating_list_copy.append(new_rating)
else:
    for rating in rating_list:
        if new_rating == rating:
            rating_index = rating_list.index(rating)
            rating_count = rating_list.count(rating)
            rang_index = rating_index + rating_count
            rating_list_copy.insert(rating_index, new_rating)
            break
        else:
            continue
print(rating_list_copy)