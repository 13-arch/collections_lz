input_data = open('input.txt', 'r')
output = open('output.txt', 'w')
data = input_data.read()
data = data.split()#разделение элементов
output.write(str('0, '))#вводим ноль запятую пробел потому что фибоначи начинается с нуля
a =int(data[0])#выводи число с файла
f1=0
f2=1
for i in range(1,a):#промежуток
    output.write(str(f1+f2) +(', '))
    if i%2 ==0 :#условие
        f1=f1+f2
    elif i%2==1:#условие
        f2=f1+f2
if (f2+f1)%2==0:
        a=(f2+f1)*2
        output.write(str(a)) 
elif (f2+f1)%2==1:
    q =(f2+f1)**2
    output.write(str(q))      
input_data.close()
output.close()