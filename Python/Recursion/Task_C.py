# C: Функция Аккермана

m = int(input("Введите m: "))
n = int(input("Введите n: "))

def Accerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Accerman(m - 1, 1)
    else:
        return Accerman(m - 1, Accerman(m, n - 1))

print(Accerman(m,n))