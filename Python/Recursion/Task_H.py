# H: Проверка числа на простоту
# Дано натуральное число n > 1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 
# Алгоритм должен иметь сложность O(n**0.5)

def test_simple(n, div = 2):
    if n == 2 or div * div > n:
        print("YES")
        return
    if n % div == 0: 
        print("NO")
        return
    test_simple(n, div + 1)    

n = int(input("Введите N: "))
test_simple(n)