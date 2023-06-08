# S: Заданная сумма цифр
# Даны натуральные числа k и s. Определите, сколько существует k-значных натуральных чисел, 
# сумма цифр которых равна s
# Запись натурального числа не может начинаться с цифры 0.
# В этой задаче можно использовать цикл для перебора всех цифр, стоящих на какой-либо позиции.

def get_num_sum(n, sum = 0):
    if n == 0:
        return sum
    return get_num_sum(n // 10, sum + n % 10)

def get_num_count(n, count, k, s):
    if n == 10**k:
        return count
    if get_num_sum(n) == s:
        count += 1
    return get_num_count(n + 1, count, k, s)    

k = int(input("k: "))
s = int(input("s: "))

print(get_num_count(10**(k-1), 0, k, s))