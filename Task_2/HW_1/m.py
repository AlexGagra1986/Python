import random


n = input("Введите количество монет ")
n = int(n)


spisok_1 = []
countZero = 1
countOne = 1

for element in range(0, n):
    k = random.randint(0, 1)
    # Для добавления элементов в список используется функция append ()
    spisok_1.append(k)
	
# теперь мы их обрабатываем-выводим
for i in spisok_1:
     print(i)
     if i == 0 :
          countZero+=1
     else:
          countOne+=1


if countZero > countOne:
     print("Минимальное количество монет которые надо перевернуть", countOne-1)
else:
     print("Минимальное количество монет которын надо перевернуть:", countZero-1)
    

