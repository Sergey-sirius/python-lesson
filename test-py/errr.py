import math;

""" Вывод чисел которые делятся на 3 или 5 без остатка """
num=1
for num in range(100):
    if not ((num % 3) and (num % 5)):
        print('=>',num, 'результат деление на 3 ->',(num/3), '    результат деление на 5 ->',(num/5) )