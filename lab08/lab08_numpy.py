import numpy as np

# ---------- Задание 1. Создание векторов и матриц ----------
hours = np.arange(0, 22, 3)            # от 0 до 21 с шагом 3
line = np.linspace(0, 1, 5)            # пять равноудалённых чисел от 0 до 1 включительно
zeros = np.zeros(6, dtype=int)         # вектор из шести нулей целого типа
unknown_table = np.full((2, 3), -1)    # матрица (2, 3), заполненная -1
identity = np.eye(3)                   # единичная матрица 3x3

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

# ---------- Задание 2. Индексы и срезы в векторе ----------
print("третий элемент:", hours[2])
print("последний элемент:", hours[-1])
print("элементы с индексами 2-5:", hours[2:6])   # правая граница не входит
print("каждый второй элемент:", hours[::2])
print("в обратном порядке:", hours[::-1])

# ---------- Задание 3. Строки и столбцы таблицы ----------
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("форма:", temperatures.shape)
print("число измерений:", temperatures.ndim)
print("число элементов:", temperatures.size)
print("вторая строка, третий столбец:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[:2, 1:3]         # строки 0 и 1, столбцы 1 и 2
print("центральный фрагмент 2x2:\n", center)
print("его форма:", center.shape)
