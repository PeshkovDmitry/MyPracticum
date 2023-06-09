# Q: Количество единиц
# Дана последовательность натуральных чисел (одно число в строке), завершающаяся двумя числами 0 подряд. 
# Определите, сколько раз в этой последовательности встречается число 1. 
# Числа, идущие после двух нулей, необходимо игнорировать.
# В этой задаче нельзя использовать глобальные переменные и параметры,
# передаваемые в функцию. Функция получает данные, считывая их с клавиатуры, 
# а не получая их в виде параметров.

def one_count(): 
    x_1 = int(input(":"))
    x_2 = int(input(":"))
    if x_1 == 0 and x_2 == 0:
        return 0
    y = one_count()
    if x_1 == 1:
        y += 1
    if x_2 == 1:
        y += 1    
    return y     

print(f"->{one_count()}")   