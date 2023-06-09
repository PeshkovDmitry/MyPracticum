# T: Без двух нулей
# Даны числа a и b. Определите, сколько существует последовательностей из 
# a нулей и b единиц, в которых никакие два нуля не стоят рядом.

def test_seq(n, twin_zero = False, count = 0): 
    if not n: 
        return (False, count)
    n_0 = n % 2
    n_short = n // 2
    n_1 = n_short % 2
    if not n_0 and not n_1:
        return (True, count)
    if n_0:
        return test_seq(n // 2, False, count + 1)
    else:
        return test_seq(n // 2, False, count)       

def count_nums(a, b, n = 0, count = 0):
    if n == 2**(a + b) - 1:
        return count
    twin_zero, count_ones = test_seq(n)  
    if not twin_zero and count_ones == b:  
        # print(f"n->{n}")   
        return count_nums(a, b, n + 1, count + 1) 
    else:
        return count_nums(a, b, n + 1, count)

a = int(input("a: "))
b = int(input("b: "))
print(count_nums(a, b, 2**(a + b) // 4)) 
