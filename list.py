input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
a = int(data)
list = []
list.append(0) #добавлем первый ноль
list.append(1) #добавлем первую единицу
f1 = 0
f2 = 1
k = 0 #количество элементов больше медианного значения
for i in range(1, a-1):

    if i%2 == 0: #если i четное, то мы обноляем s1
        f1=f1+f2
    elif i%2 == 1: #если i нечетное, то мы обноляем s2(чередуем после каждого числа)
        f2=f1+f2
    list.append(f1+f2)
i = 0
for i in range(0, len(list)): 
    if list[i] % 2 == 0: #проверяем на четность
        list[i] = list[i] * 2 #если четное, то умножаем на 2
    else:
        list[i] = list[i] ** 2 #если нечетное, то возводим в квадрат
i = 0
minel = min(list) #минмимальный элемент
maxel= max(list) #максимальный элемент
lenl = len(list) #длина списка
arifm = sum(list)/len(list) #медианное значение
for i in range(0, len(list)):
    if int(list[i]) > arifm:
        k += 1 #проверяем, сколько чисел бедет больше мидианного значения
output.write(str('min - ') + str(minel) + str('\nmax - ') + str(maxel) + str('\nlen - ') + str(lenl) + str('\n> median - ') + str(k))
input_data.close()
output.close()