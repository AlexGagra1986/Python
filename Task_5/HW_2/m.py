# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

n = int(input('Введите количество грядок: '))
if n < 3: 
    print('Грядок должно быть больше двух')
else:
    arr = []
    for i in range(n):
        arr.append(int(input('Введите количество ягод: ')))

    first_num = arr[0] + arr[1] + arr[n-1]
    last_num = arr[0] + arr[n-2] + arr[n-1]

    max_num = 0

    if first_num > last_num:
        max_num = first_num
    else: 
        max_num = last_num    
    for i in range(1, n-1):
        if max_num < arr[i] + arr[i-1] + arr[i+1]:
            max_num = arr[i] + arr[i-1] + arr[i+1]
    print(max_num)