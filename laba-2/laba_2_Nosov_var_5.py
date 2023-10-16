# Вариант 5(15 в списке)

# Задание 1
from math import *

print("Задание 1\n")
args = []
alf = 'xyz'
for i in range(3):
    print(f"Задайте переменную %s:" % alf[i])
    args.append(float(input()))

a = (2 * cos(args[0] - (pi / 6)) ** 4) / (1 / 2 + sin(args[1]) ** 2)
print("Значение выражения а = " + str(a))

b = 1 + (args[2] ** 2) / (3 + (args[2] ** 2) / 5)
print("Значение выражения b = " + str(b))

# Задание 2
print("\n\nЗадание 2\n")
a, b, c, x, h = 2, 1, -1, 2, 0.05

f1 = sqrt((x ** 2 + a * x) / b + c * x ** 2)
f2 = sqrt(((x + h) ** 2 + a * (x + h)) / b + c * (x + h) ** 2)

print("Значение выражения f(2) = " + str(f1))
print("Значение выражения f(2.05) = " + str(f2))

# Задание 3
print("\n\nЗадание 3\n")
for x in range(10, 31):
    print(f"f({(x / 10)}) = " + str(tan(abs(log((x / 10) ** 2, e))) ** 2))

# Задание 4
print("\n\nЗадание 4\n")
xy = []
for i in range(3):
    print(f"Задайте переменную x{i + 1}:")
    xy.append(float(input()))
    print(f"Задайте переменную y{i + 1}:")
    xy.append(float(input()))

a = sqrt((xy[0] - xy[2]) ** 2 + (xy[1] - xy[3]) ** 2)
b = sqrt((xy[2] - xy[4]) ** 2 + (xy[3] - xy[5]) ** 2)
c = sqrt((xy[4] - xy[0]) ** 2 + (xy[5] - xy[1]) ** 2)
p = (a + b + c) / 2
r = sqrt(p * (p - a) * (p - b) * (p - c)) / p
print("Радиус вписанной окружности r = " + str(r))

# Задание 5
print("\n\nЗадание 5\n")
args = []
g = 6.67 * 10 ** -11
alf = ('m1', 'm2', 'r')
for i in range(3):
    print(f"Задайте переменную %s:" % alf[i])
    args.append(float(input()))
f = g * args[0] * args[1] / args[2] ** 2
print("Сила притяжения F = " + str(f))

# Задание 6
print("\n\nЗадание 6\n")
a = 0
while (a < 1 or a > 100):
    print("Введите a в диапазоне (1 <= a <= 100):")
    a = float(input())
print(str(a ** 3) + " " + str(6 * a ** 2))

# Задание 7
print("\n\nЗадание 7\n")
xy = []
alf = ("x1", "y1", "x2", "y2")
i = 0
print("-100<=x1,y1,x2,y2<=100")
while (len(xy) != 4):
    print(f"Задайте координату %s:" % alf[i])
    xy.append(float(input()))
    if (xy[i] >= -100 and xy[i] <= 100):
        i += 1
    else:
        xy.pop(i)

h = sqrt((xy[2] - xy[0]) ** 2 + (xy[3] - xy[1]) ** 2)
print(f"{h:.5f}")

# Задание 8
print("\n\nЗадание 8\n")
alf = ("V", "U", "T1", "T2")
args = []
print("Переменные - натуральные числа, U < V")
i = 0
while (len(args) != 4):
    print(f"Задайте переменную %s:" % alf[i])
    args.append(abs(float(input())))
    if (i != 1 or args[i - 1] > args[i]):
        i += 1
    else:
        args.pop(i)

S = args[2] * (args[0] + args[1]) + args[3] * (args[0] - args[1])
print(f"S = {S:.4}")

# Задание 9
print("\n\nЗадание 9\n")
print(f"Первый рабочий, работавший 2 недели, заработал {90000 / 3} рублей.\n"
      f"Второй рабочий, работавший 4 недели, заработал {90000 * 4 / 6} рублей.")

