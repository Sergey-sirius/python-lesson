
#
print('=== boollean 1')
print(bool(""), bool([]), bool(()))
# result False False False

#
print('=== сравнение 1 == 1, 1 == 5')
print(1 == 1, 1 == 5)
#result True False

#
print('=== in — проверка на вхождение в последовательность')
print(2 in [1, 2, 3], 4 in [1, 2, 3])
# result True False

#
print('=== is — проверяет, ссылаются ли две переменные на один и тот же объект.')
x = y = [1, 2]
print(x is y)
# result True
x = [1, 2]; y = [1, 2]
print(x is y)
# result False

#
print('=== интерпретатор производит кэширование малых целых чисел и небольших строк')
x = 2; y = 2; z = 2
print(x is y, y is z)
# result True True

# Перечислим операторы сравнения в порядке убывания приоритета:
    # 1. <, >, <=, >=, ==, !=, <>, is, is not, in, not in.
    # 2. not — логическое отрицание.
    # 3. and — логическое И.
    # 4. or — логическое ИЛИ.

# IF
    # x = int(input("Введите число: "))
    # if x % 2 == 0:
    #     print(x, " - четное число")
    # else:
    #     print(x, " - нечетное число")

    #  IF 2
    # print("""Какой операционной системой вы пользуетесь?
    # 1 — Windows 10
    # 2 — Windows 8.1
    # 3 — Windows 8
    # 4 — Windows 7
    # 5 — Windows Vista
    # 6 — Другая""")
    # os = input("Введите число, соответствующее ответу: ")
    # if os == "1":
    #     print("Вы выбрали: Windows 10")
    # elif os == "2":
    #     print("Вы выбрали: Windows 8.1")
    # elif os == "3":
    #     print("Вы выбрали: Windows 8")
    # elif os == "4":
    #     print("Вы выбрали: Windows 7")
    # elif os == "5":
    #     print("Вы выбрали: Windows Vista")
    # elif os == "6":
    #     print("Вы выбрали: другая")
    # elif not os:
    #     print("Вы не ввели число")
    # else:
    #     print("Мы не смогли определить вашу операционную систему")
    # input()
    # ctrl+/

# 2
print('=== if 2')
print("Yes" if 10 % 2 == 0 else "No")
# result Yes

#
print('===  Цикл 1')
for s in "str":
    print(s, end=" ")
else:
    print("\nЦикл выполнен")
# result s t r

#
print('===  Array')
arr = {"x": 1, "y": 2, "z": 3}
arr.keys()
for key in sorted(arr):
    print(key, arr[key])
# result
# x 1
# y 2
# z 3



