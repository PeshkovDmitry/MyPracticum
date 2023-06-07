# B: От A до B
# Даны два целых числа A и В (каждое в отдельной строке). 
# Выведите все числа от A до B включительно, в порядке возрастания, 
# если A < B, или в порядке убывания в противном случае.

def up(num, a, b):
    if num > b:
        return
    print(num)
    up(num + 1, a, b)   

def down(num, a, b):
    if num < b:
        return
    print(num)
    down(num - 1, a, b)     

a = int(input("Введите A: "))
b = int(input("Введите B: "))

if (a > b):
    down(a,a,b)
else:    
    up(a,a,b)