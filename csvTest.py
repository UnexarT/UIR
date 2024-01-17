import csv
import statistics as stat

students = []

with open('studentsInfo.csv') as csvfile:
    students = [row for row in csv.DictReader(csvfile)]

keys = list(students[0])
disciplines = keys[1:]

def SumGrades(student):
    return sum([int(student[discipline]) for discipline in disciplines])

def GradeModa(discipline):
    '''moda = {}
    moda[discipline] = stat.mode([int(student[discipline]) for student in students])
    return moda'''
    return stat.mode([int(student[discipline]) for student in students])

def GradeMax(discipline):
    '''Max = {}
    Max[discipline] = max([int(student[discipline]) for student in students])
    return Max'''
    return max([int(student[discipline]) for student in students])

def GradeMin(discipline):
    '''Min = {}
    Min[discipline] = min([int(student[discipline]) for student in students])
    return Min'''
    return min([int(student[discipline]) for student in students])

def GradeMiddle(discipline):
    '''Max = {}
    middle[discipline] = stat.median([int(student[discipline]) for student in students])
    return Max'''
    return stat.median([int(student[discipline]) for student in students])

#mode - критерий суммы по предметам
#      0 - все
#      1 - Математика
#      2 - ИСИС
#      3 - Социология
#      4 - ИГКГ
#      5 - ЯПМТ
#      6 - Курсовая по ЯПМТ

def sortByGrades(mode, reverse = False):                     #сортировка Пузырьком
    studentsCopy = students.copy()
    if mode == 0:
        for i in range(len(studentsCopy) - 1):
            for j in range(i + 1, len(studentsCopy)):
                if SumGrades(studentsCopy[i]) > SumGrades(studentsCopy[j]):
                    studentsCopy[i],studentsCopy[j] = studentsCopy[j],studentsCopy[i]
    elif mode > 0 and mode < 7:
        for i in range(len(students) - 1):
            for j in range(i + 1, len(students)):
                if studentsCopy[i][disciplines[mode-1]] > studentsCopy[j][disciplines[mode-1]]:
                    studentsCopy[i],studentsCopy[j] = studentsCopy[j],studentsCopy[i]
    else:
        print("Абасрался чухан")

    return studentsCopy[::-1] if reverse else studentsCopy

#След функции выводят массив: 0 индекс - название предмета, 1 индекс - значение функции(max, min, moda, mid),
#                             индексы со 2 - ФИО студентов подходящих под критерии функции

def Middle(mode):
    if mode == 0:
        grades = [GradeMiddle(discipline) for discipline in disciplines]
        middle = ['По всем',stat.median(grades)]
        for student in students:
            StudDrades = [int(student[discipline]) for discipline in disciplines]
            if middle[1] in StudDrades: middle.append(student[keys[0]])
        return middle
    elif mode > 0 and mode < 7:
        middle = [disciplines[mode-1],GradeMiddle(disciplines[mode-1])]
        for student in students:
            if middle[1] == int(student[middle[0]]): middle.append(student[keys[0]])
        return middle
    else:
        print("Абасрался чухан")

def Min(mode):
    if mode == 0:
        grades = [GradeMin(discipline) for discipline in disciplines]
        Min = ['По всем',min(grades)]
        for student in students:
            StudDrades = [int(student[discipline]) for discipline in disciplines]
            if Min[1] in StudDrades: Min.append(student[keys[0]])
        return Min
    elif mode > 0 and mode < 7:
        Min = [disciplines[mode-1],GradeMin(disciplines[mode-1])]
        for student in students:
            if Min[1] == int(student[Min[0]]): Min.append(student[keys[0]])
        return Min
    else:
        print("Абасрался чухан")

def Max(mode):
    if mode == 0:
        grades = [GradeMax(discipline) for discipline in disciplines]
        Max = ['По всем',max(grades)]
        for student in students:
            StudDrades = [int(student[discipline]) for discipline in disciplines]
            if Max[1] in StudDrades: Max.append(student[keys[0]])
        return Max
    elif mode > 0 and mode < 7:
        Max = [disciplines[mode-1],GradeMax(disciplines[mode-1])]
        for student in students:
            if Max[1] == int(student[Max[0]]): Max.append(student[keys[0]])
        return Max
    else:
        print("Абасрался чухан")

def Moda(mode):
    if mode == 0:
        grades = [GradeModa(discipline)[discipline] for discipline in disciplines]
        moda = ['По всем',stat.mode(grades)]
        for student in students:
            StudDrades = [int(student[discipline]) for discipline in disciplines]
            if moda[1] in StudDrades: moda.append(student[keys[0]])
        return moda
    elif mode > 0 and mode < 7:
        moda = [disciplines[mode-1],GradeModa(disciplines[mode-1])]
        for student in students:
            if moda[1] == int(student[moda[0]]): moda.append(student[keys[0]])
        return moda
    else:
        print("Абасрался чухан")
print(Middle(2))


