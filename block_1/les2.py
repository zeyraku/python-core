# goods_cost = 4200
# if goods_cost >= 10_000:
#     print(f'Скидка 15%, итоговая сумма: {goods_cost * 0.85}')
# elif goods_cost >= 5000:
#     print(f'Скидка 10%, итоговая сумма: {goods_cost * 0.9}')
# elif goods_cost >= 1000:
#     print(f'Скидка 5%, итоговая сумма: {goods_cost * 0.95}')
# else:
#     print(f'Скидки нет, сумма: {goods_cost}')


# n = int(input('Введите число: '))
# for i in range(n,0,-1):
#     print(i)


# n = int(input('Введите n: '))
# col = 0
# for i in range(1,n+1):
#     if i % 3 == 0:
#         col += 1
#     else:
#         continue
# print(col)


# while True:
#     num = float(input('Введите число: '))
#     if num > 0:
#         print(num ** 2)
#     elif num < 0:
#         continue
#     else:
#         print('Программа завершена')
#         break


# for i in range(1,5+1):
#     for j in range(1,5+1):
#         print(i * j, end = " ")
#     print()


# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print('*', end = "")
#     print()



# n = int(input('Введите число: '))
# col = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)
#         col += 1
# print(f'Количество делителей: {col}')



# col = 0
# s_plus = 0
# col_otr = 0
# max_num = None
# previous_num = None
# col_difference = 0

# while True:
#     num = int(input('Введите число: '))

#     if num == 0:
#         break

#     col += 1

#     # Сумма положительных и количество отрицательных
#     if num > 0:
#         s_plus += num
#     else:
#         col_otr += 1

#     # Поиск максимального числа
#     if max_num is None or num > max_num:
#         max_num = num

#     # Сравнение с предыдущим числом
#     if previous_num is not None:
#         if num > previous_num:
#             col_difference += 1

#     # Сохраняем число для следующей итерации
#     previous_num = num

# print(f'Количество чисел: {col}')
# print(f'Сумма положительных: {s_plus}')
# print(f'Количество отрицательных: {col_otr}')
# print(f'Максимальное число: {max_num}')
# print(f'Количество увеличений: {col_difference}')


# col = 0
# time_col = 1
# prev = None
# while True:
#     num = int(input('Введите число: '))
#     if num == 0:
#         break
#     if prev is not None:
#         if num == prev:
#             time_col += 1
#         else:
#             time_col = 1
#     if time_col > col:
#         col = time_col
#     prev = num
# print(f'Максимальное количество подряд идущих: {col}')
            







