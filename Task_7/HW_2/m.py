#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

x = input("Введите элементы списка через пробел ").split()
min = int(input("Введите минимальный предел"))
max = int(input("Введите максимальный предел"))

listN = list(map(int, x))


def index(list,min,max):
 arrBuf = []
 for i in range(len(list)):
    if min <= list[i] <= max:
        arrBuf.append(list[i])
 return arrBuf

print(index(listN,min,max))






