# I: Разложение на множители
# Дано натуральное число n > 1. Выведите все простые делители этого числа 
# в порядке неубывания с учетом кратности. Алгоритм должен иметь сложность O(n**0.5)

def get_dividers(n, div = 2):
    if n == 1:
        return
    if n % div == 0:
        print(div)
        get_dividers(n / div, div)
    else:
        get_dividers(n, div + 1)

n = int(input("Введите N: "))
get_dividers(n)