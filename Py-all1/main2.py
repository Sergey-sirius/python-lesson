
#
print('=== Функции range() и enumerate()')
arr = [1, 2, 3]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)
# result [2, 4, 6]

#
print('===  range 2')
for i in range(1, 4): print(i)
# result
# 1
# 2
# 3

#
print('===  range 3')
for i in range(4, 0, -1): print(i)
# result
# 4
# 3
# 2
# 1

#
print('===  range 4')
obj = range(len([1, 2, 3]))
print(obj[0], obj[1], obj[2])
# result
# 0 1 2

#
print('===  range 3')
i = iter(obj)
print(next(i), next(i), next(i))
# result
# 0 1 2

#
print('=== index(<Значение>) — возвращает индекс элемента, имеющего указанное значение')
arr = [1, 2, 3, 4]
print(arr.index(1), arr.index(4))
# result 0 3
#print(arr.index(5))
# result ValueError: 5 is not in list

#
print('=== count')
arr = [1, 2, 2, 3, 5]
print(arr.count(1), arr.count(2))
# result 1 2

#

