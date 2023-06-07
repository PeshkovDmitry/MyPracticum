# A: От 1 до n
# Дано натуральное число n. Выведите все числа от 1 до n.

def show_num(num):
    if num == 1: 
        print(num)
        return
    show_num(num - 1)
    print(num)  

n = int(input("Введите n: "))
show_num(n)