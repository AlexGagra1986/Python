#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
def degree(a, b):
    res = a**b
    return abs(res)

    
print(degree(a,b)) 