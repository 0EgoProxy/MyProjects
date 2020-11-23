import numpy as np

# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def task_func(x: float):
    y = np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)
    return y  # round(y, 4)


print('Введите размерность матрицы.')
n = int(input())

print('Введите: "X"')
x = int(input())

matrix = np.array([[x for i in range(n)] for j in range(n)])
power = 0
for i in matrix:
    for j in range(len(i)):
        i[j] = i[j] ** power
        power += 1
print(matrix)

print('Введите свой вектор \n:')
vector = np.array([int(input()) for i in range(n)])
