# #* 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

# entered_day = int(input('Введите номер дня: '))

# # print(['нет', 'да'][entered_day % 7 == 0 or entered_day % 7 == 6])

# if entered_day % 7 == 0 or entered_day % 7 == 6:
#     print('да')
# else:
#     print('нет')


#* 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# from itertools import product


# def de_morgan_law(x, y, z):
#     left_part = not (x or y or z)
#     right_part = (not x) and (not y) and (not z) # Скобки просто для удобства чтения
#     return left_part == right_part

# # combinations = product([0, 1], [0, 1], [0, 1])

# # for combination in combinations:
# #     print(f'{combination} -> {de_morgan_law(combination[0], combination[1], combination[2])}')

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'({x}, {y}, {z}) -> {de_morgan_law(x, y, z)}')

#* 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)

# x_coord = int(input('Введите х точки: '))
# y_coord = int(input('Введите у точки: '))

# if (not x_coord) and y_coord:
#     print(f'Точка ({x_coord}, {y_coord}) лежит на оси Х')
# elif (not y_coord) and x_coord:
#     print(f'Точка ({x_coord}, {y_coord}) лежит на оси Y')
# elif x_coord > 0:
#     if y_coord > 0:
#         print(f'Точка ({x_coord}, {y_coord}) находится в I четверти')
#     else:
#         print(f'Точка ({x_coord}, {y_coord}) находится в IV четверти')
# elif x_coord < 0:
#     if y_coord > 0:
#         print(f'Точка ({x_coord}, {y_coord}) находится во II четверти')
#     else:
#         print(f'Точка ({x_coord}, {y_coord}) находится в III четверти')
# else:
#     print(f'Координаты не должны одновременно быть равны 0!')


#* 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

# quarter = input('Введите номер четверти (1-4): ')

# if quarter == '1':
#     print('Диапазон координат в I четверти:\nX - (0, +∞)\nY - (0, +∞)')
# elif quarter == '2':
#     print('Диапазон координат во II четверти:\nX - (-∞, 0)\nY - (0, +∞)')
# elif quarter == '3':
#     print('Диапазон координат в III четверти:\nX - (-∞, 0)\nY - (-∞, 0)')
# elif quarter == '4':
#     print('Диапазон координат в IV четверти:\nX - (0, +∞)\nY - (-∞, 0)')
# else:
#     print('Неверный номер четверти!')


#* 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
from math import floor


def calculate_distance(point_1, point_2, sign_digs=2):
    dx = abs(point_1[0] - point_2[0])
    dy = abs(point_1[1] - point_2[1])

    return int(((dx ** 2 + dy ** 2) ** 0.5) * 10 ** sign_digs) / 10 ** sign_digs
# Считаю, что первый пример работы на сайте выполнен не совсем правильно (5.09 без этих извращений не получить)
# На всякий случай, (7,-5) -> (1,-1) = 5.09901......



first_point = int(input('Введите х 1 точки: ')), int(input('Введите у 1 точки: '))
second_point = int(input('Введите х 2 точки: ')), int(input('Введите у 2 точки: '))

print(f'Расстояние между точками {first_point} и {second_point} равно \
{calculate_distance(first_point, second_point)}')