def hash1(str):
    return 1

def hash2(str):
    return len(str)

mas = [1,2,3,4,5,6,7]
print(mas[hash2("apple")])

def hash3(str, mas1, mas2):
    list = []
    if str[0] in mas1:
        list = mas2[mas1.index(str[0])]
        list.append(str)
        mas2[mas1.index(str[0])] = list
    else:
        mas1.append(str[0])
        list.append(str)
        mas2.append(list)

mas1 = []
mas2 = []

hash3("apple", mas1, mas2)
hash3("avocado", mas1, mas2)
hash3("banana", mas1, mas2)
hash3("blackberry", mas1, mas2)
print(mas1)
print(mas2)


def hash4(str):
    hash = int(input("Введите размер хэша: "))
    letters = "abcdefghijklmnopqrstuvwxyz"
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47
        ,53,59,61,67,71,73,79,83,89,97,101]
    sum = 0
    for i in str:
        sum += primes[letters.index(i)]
    return sum%hash

print(hash4("bag"))

def hash5(key, value, keys, values):
    list = []
    if key in keys:
        list = values[keys.index(key)]
        list.append(value)
        values[keys.index(key)] = list
    else:
        keys.append(key)
        list.append(value)
        values.append(list)

names = []
numbers = []

hash5("Esther", "89091545616", names, numbers)
hash5("Ben", "89091545617", names, numbers)
hash5("Bob", "89091545618", names, numbers)
hash5("Dan", "89091545619", names, numbers)
hash5("Dan", "89091545620", names, numbers)

print(names)
print(numbers)

batteries = []
voltages = []

hash5("A", 1.5, batteries, voltages)
hash5("AA", 1.5, batteries, voltages)
hash5("AAA", 1.5, batteries, voltages)
hash5("AAAA", 9, batteries, voltages)

print(batteries)
print(voltages)

writers = []
works = []

hash5("Maus", "Art Spiegelman", works, writers)
hash5("Fun Home", "Alison Bechdel", works, writers)
hash5("Watchmen", "Alan Moore", works, writers)

print(works)
print(writers)
