from scipy import optimize

""" Решение оптимизационных задач в SciPy """
""" Функция Розенброка """


def func_rozenbroca(x):
    return .5 * (1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2


# print(func_rozenbroca([1, 1]))
# result = optimize.brute(func_rozenbroca, ((-5, 5), (-5, 5)))
# print(result)

# print(optimize.differential_evolution(func_rozenbroca, ((-5, 5), (-5, 5))))

# print(optimize.minimize(func_rozenbroca, [2, 2], method='BFGS', jac='g'))
# jac - параметр для указания градиента или нет
# method='BFGS' - просто название метода. Их множество и можно посмотреть их в функции "minimize"

print(optimize.minimize(func_rozenbroca, [2, 2], method='Nelder-Mead'))