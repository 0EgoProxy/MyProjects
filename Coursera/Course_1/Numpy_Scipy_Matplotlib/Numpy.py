import numpy as np

m = [1, 2, 3, 4, 5]
y = np.array(m)

# print(type(m), m, type(y), y)
# print(m[1:3])
# print(y[1:3])ц

# print(y[[0, 2]])
# print(y[y>3])  # Логическими операциями, где True выведет, False не подаст на вывод
""" Так же можно использовать numpy и для умножения элементов массива на n число или возведение его в n-степень """
# print(y ** 2)

"""Квадраты чисел"""
# print(np.arange(1, 101) ** 2)
# print(np.arange(0, 8, 0.1))  # можно использовать значения в шаге не равные целым числам.

sp1 = [1, 2, 3, 4]
sp2 = [2, 4, 6, 8]
sp1 = np.array(sp1)
sp2 = np.array(sp2)

result = sp1 * sp2
print(result)
