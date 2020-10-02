#!/usr/bin/env python3
import math
print('Введите коэфиценты квадратного уравнения')
a=1
b=input('Введите коэфицент b = ')
c=input('Введите коэфицент c = ')
a=int(a)
b=int(b)
c=int(c)

print('\n цикл while')
while a<10:
    print('Решение уравнения при a = ',a)
    d=b*b-4*a*c
    print('Дискриминант = ', d)
    if (d>0):
        x=(-b+math.sqrt(d))/(2*a)
        y=(-b-math.sqrt(d))/(2*a)
        print('Первый корень = ', x)
        print('Второй корень = ', y,"\n")
    elif (d==0):
        x=-b/(2*a)
        print('Корень уравнения - ', x,'\n')
    else:
        print('Уравнение не имеет корней\n')
    a=a+1

print('\n цикл for')
a=1
for a in [1,2,3,4,5,6,7,8,9]:
    print('Решение уравнения при a = ',a)
    d=b*b-4*a*c
    print('Дискриминант = ', d)
    if (d>0):
        x=(-b+math.sqrt(d))/(2*a)
        y=(-b-math.sqrt(d))/(2*a)
        print('Первый корень = ', x)
        print('Второй корень = ', y,"\n")
    elif (d==0):
        x=-b/(2*a)
        print('Корень уравнения - ', x,'\n')
    else:
        print('Уравнение не имеет корней\n')
    a=a+1