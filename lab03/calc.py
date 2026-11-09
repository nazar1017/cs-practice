def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


a = float(input("Первое число: "))
b = float(input("Второе число: "))
print("Сумма:", add(a, b))
print("Разность:", subtract(a, b))
print("Произведение:", multiply(a, b))


def safe_divide(a, b):
    if b == 0:
        return None
    return a / b


quotient = safe_divide(a, b)
print("Частное:", "деление на ноль невозможно" if quotient is None else quotient)
