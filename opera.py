from z3 import *
# The operator that the enumrate algorithm used


def Add(a, b):
    return a+b


def Sub(a, b):
    return a-b


def Inc(a):
    a = a+1
    return a


def Dec(a):
    a = a - 1


def Mod(a, b):
    return a % b


def Ge(a, b):
    return a >= b


def Gt(a, b):
    return a > b


def Equal(a, b):
    return a == b


def Unequal(a, b):
    return a != b


def OR(a, b):
    return (a or b)


def z3OR(a, b):
    return Or(a, b)


def AND(a, b):
    return (a and b)


def z3AND(a, b):
    return And(a, b)


def NOT(a):
    return (not a)


def z3NOT(a):
    return Not(a)


def Zero():
    return 0


def ITE(c, a, b):
    if (c):
        return a
    else:
        return b


def z3ITE(c, a, b):
    return If(c, a, b)


def One():
    return 1


def Two():
    return 2


def Three():
    return 3


def Four():
    return 4


def Five():
    return 5


def Six():
    return 6


def Seven():
    return 7


def Eight():
    return 8


def Nine():
    return 9


def ModTest(a, b, c):
    return a % b == c


def number0():
    return 0


def number1():
    return 1


def number2():
    return 2


def number3():
    return 3


def number4():
    return 4


def number5():
    return 5


def number6():
    return 6


def number7():
    return 7


def number8():
    return 8


def number9():
    return 9


def number10():
    return 10


def number11():
    return 11


def number12():
    return 12


def number13():
    return 13


def number14():
    return 14


def number15():
    return 15


def number16():
    return 16


def number17():
    return 17


def number18():
    return 18


def number19():
    return 19


def number20():
    return 20


def number21():
    return 21


def number22():
    return 22


def number23():
    return 23


def number24():
    return 24


def number25():
    return 25


def number26():
    return 26


def number27():
    return 27


def number28():
    return 28


def number29():
    return 29


def number30():
    return 30


def number31():
    return 31


def number32():
    return 32


def number33():
    return 33


def number34():
    return 34


def number35():
    return 35


def number36():
    return 36


def number37():
    return 37


def number38():
    return 38


def number39():
    return 39


def number40():
    return 40


def number41():
    return 41


def number42():
    return 42


def number43():
    return 43


def number44():
    return 44


def number45():
    return 45


def number46():
    return 46


def number47():
    return 47


def number48():
    return 48


def number49():
    return 49


def number50():
    return 50


def number51():
    return 51


def number52():
    return 52


def number53():
    return 53


def number54():
    return 54


def number55():
    return 55


def number56():
    return 56


def number57():
    return 57


def number58():
    return 58


def number59():
    return 59


def number60():
    return 60


def number61():
    return 61


def number62():
    return 62


def number63():
    return 63


def number64():
    return 64


def number65():
    return 65


def number66():
    return 66


def number67():
    return 67


def number68():
    return 68


def number69():
    return 69


def number70():
    return 70


def number71():
    return 71


def number72():
    return 72


def number73():
    return 73


def number74():
    return 74


def number75():
    return 75


def number76():
    return 76


def number77():
    return 77


def number78():
    return 78


def number79():
    return 79


def number80():
    return 80


def number81():
    return 81


def number82():
    return 82


def number83():
    return 83


def number84():
    return 84


def number85():
    return 85


def number86():
    return 86


def number87():
    return 87


def number88():
    return 88


def number89():
    return 89


def number90():
    return 90


def number91():
    return 91


def number92():
    return 92


def number93():
    return 93


def number94():
    return 94


def number95():
    return 95


def number96():
    return 96


def number97():
    return 97


def number98():
    return 98


def number99():
    return 99

# -----------------------------------------------------------------
