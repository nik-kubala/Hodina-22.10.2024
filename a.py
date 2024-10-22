import random
def scitavanie():
    x = 0
    y = 0
    while x < 500:
        temp = int(input("Zadaj mi celé číslo"))
        if temp % 10 == 3:
            x = x + temp
            y = y + 1
    print(x / y)

#scitavanie()

random.randrange(1, 100)                    # ako for i in range

def priemerNahodnych():
    a = 0
    b = 0
    for i in range (1, 101):
        a = a + random.randrange(1, 11)
        b = b + 1
    print(a / b)

#priemerNahodnych()

def kocka0():
    a = 0   # 1
    b = 0   # 2
    c = 0   # 3
    d = 0   # 4
    e = 0   # 5
    f = 0   # 6
    for i in range (0, 101):
        temp = random.randrange(1, 7)
        if temp == 1:
            a += 1
        if temp == 2:
            b += 1
        if temp == 3:
            c += 1
        if temp == 4:
            d += 1
        if temp == 5:
            e += 1
        if temp == 6:
            f += 1



jozo = []                       # zoznam
for i in range (0, 6):
    jozo.append(0)              # pridavam domceky s hodnotou 0, in range 0-6 takze 6 domcekov
#print jozo


for i in range (0, 100):
    temp = random.randrange(1, 7)
    jozo[temp - 1] = jozo[temp - 1] + 1

#print(jozo)

def kocka1():
    jozo = []
    for i in range(0, 6):
        jozo.append(0)
    for i in range(0, 100):
        temp = random.randrange(1, 7)
        jozo[temp - 1] = jozo[temp - 1] + 1
    print(jozo)
kocka1()


def disrkiminant():
    a = float(input("Zadaj hodnotu a:"))
    b = float(input("Zadaj hodnotu b:"))
    c = float(input("Zadaj hodnotu c:"))
    D = b ** 2 - 4 * a * c
    if D > :
        print("x1 =", (-b + (D ** 0.5)) / 2 * a)
        print("x2 =", (-b - (D ** 0.5)) / 2 * a)