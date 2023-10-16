import random

def inp(a,b):
    flag = True
    while flag:
        inp = input("Ваш выбор: ")
        if inp.isdigit():
            inp = int(inp)
            if inp > a-1 and inp < b+1: flag = False
    return inp
def game():
    print("\nВыберите предмет\n"
          "1 - камень\n"
          "2 - ножници\n"
          "3 - бумага")
    inv = ("камень", "ножници", "бумагу")
    plr = inp(1,3)
    print(f"Вы выбрали {inv[plr-1]}")
    comp = random.randint(1,3)
    print(f"Компьютер выбрал {inv[comp-1]}")
    win = 0
    if plr == comp: win = 0
    elif plr == 1 and comp == 2: win = 1
    elif plr == 1 and comp == 3: win = 2
    elif plr == 2 and comp == 1: win = 2
    elif plr == 2 and comp == 3: win = 1
    elif plr == 3 and comp == 1: win = 1
    else: win = 2

    if win == 0: print("\nНичья!")
    elif win == 1: print("\nПобедил игрок!")
    else: print("\nПобедил компьютер!")
    return win
def newgame():
    game()
    print("\nХотите продолжить игру?\n"
          "1 - да\n"
          "2 - нет")
    fl = inp(1,2)
    if fl == 1: newgame()
    else: print("Спасибо за игру!")
def gaming():
    print("\nВыберите режим игры\n"
          "1 - обычная игра\n"
          "2 - турнир")
    mod = inp(1,2)
    if mod == 2:
        rounds = "0"
        flag = True
        while flag:
            rounds = input("Введите кол-во раундов: ")
            if rounds.isdigit():
                rounds = int(rounds)
                if rounds > 0: flag = False
        count1, count2 = 0, 0
        for i in range(1, rounds+1):
            print(f"\nРаунд №{i}!")
            p = game()
            if p == 1: count1+=1
            elif p == 2: count2+=1
        if count1 < count2: print(f"Победа компьютера со счетом {count2}/{count1}")
        elif count1 > count2: print(f"Победа игрока со счетом {count1}/{count2}")
        else:
            p = 0
            print(f"Игра до первой победы!")
            while p < 1 or p > 2:
                rounds += 1
                print(f"\nРаунд №{rounds}!")
                p = game()
            if p == 1:
                count1 += 1
                print(f"Победа игрока со счетом {count1}/{count2}")
            else:
                count2 += 1
                print(f"Победа компьютера со счетом {count2}/{count1}")
    else: newgame()

gaming()
