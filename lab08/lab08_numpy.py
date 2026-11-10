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

# ---------- Задание 4. Прямоугольные срезы ----------
matrix = np.arange(1, 26).reshape(5, 5)
print("matrix:\n", matrix)

first_rows = matrix[:3]
print("первые три строки:\n", first_rows, first_rows.shape)

last_rows = matrix[-2:]
print("последние две строки:\n", last_rows, last_rows.shape)

first_cols = matrix[:, :2]
print("первые два столбца:\n", first_cols, first_cols.shape)

block = matrix[1:4, 2:5]               # строки 1-3, столбцы 2-4
print("строки 1-3, столбцы 2-4:\n", block, block.shape)

corner = matrix[-2:, -2:]              # правый нижний угол 2x2
print("правый нижний угол:\n", corner, corner.shape)

# ---------- Задание 5. Изменение массива с помощью срезов ----------
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)

# .copy() нужна, потому что срез и присваивание меняют массив на месте:
# без копии мы испортили бы исходный hours, а так он остаётся прежним.
changed_hours = hours.copy()
changed_hours[2:5] = 99                # элементы с индексами 2-4
changed_hours[::2] = -1                # каждый второй, начиная с первого
print("changed_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0               # вся вторая строка
changed_matrix[:, -1] = -1             # последний столбец
changed_matrix[1:4, 1:4] = 100         # центральный блок 3x3
print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)

# ---------- Задание 6. Изменение формы ----------
numbers = np.arange(12)                # числа от 0 до 11
table = numbers.reshape(3, 4)
transposed = table.T
print("numbers:", numbers.shape)
print("table:", table.shape)
print("transposed:", transposed.shape)
# reshape(3, 4) работает, потому что 3 * 4 = 12 равно числу элементов в numbers.
# reshape(5, 3) вызовет ошибку: 5 * 3 = 15, а элементов только 12,
# поэтому все элементы нельзя разложить по такой форме.
