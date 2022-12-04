#Task1
print("Hello World!")

#Task2
a=input("Task 2")
a=input('(3+8)/(4-2)*4=> ')
a=(3+8)/(4-2)*4 
print("answer", a)

#Task2.1
from math import *
a=input("Task 2.1")
print("a circle inside a square")
s=input('the area of the circle=>')
S=pi*9
print("answer", S)
print()
c=input('circle circumference=>')
C=2*pi*3
print("answer", C)
print()
print ("the area of the square")
S=input('=>')
S=4*9
print("answer", S)
print()
print("the perimeters of the square")
P=('=>')
P=8*3
print("answer", P)

#Task2.2
print()
a=input("Task 2.2")
K=input("number of coins per kilometer")
K=('=>')
K=10000/2.5
print("that´s the number of coins per kilometer", K)
K1=input("the number of coins on the equator")
K1=('=>')
K1=4000*6378
print("fit all over the equator", K1)

#Task3
a=input("Task 3")
text=("kill-koll kill-koll killadi-koll")
print(text*3)

#Task4
a=input("Task 4")
text=("Rong see sõitis tsuhh tsuhh tsuhh, piilupart oli rongijuht.Rattad tegid rat tat taa, rat tat taa ja tat tat taa.Aga seal rongi peal,kas sa tead, kes olid seal?")
print(text*1)

#Task 4.1
a=input("Task 4.1")
text1=("Rong see sõitis")
text2=("tuut tuut tuut,")
text3=("piilupart oli rongijuht. Rattad tegid kill koll koll,")
text4=("kill koll koll ja kill koll koll")
print(text1+text2+text3+text4*1)

#Task 5
from math import *
c=input("Task 5")
print("add lengths of adjacent sides of a rectangle")
a=float(input('length of the inserted rectangle=>'))
b=float(input('width of the rectangle inside=>'))
P=2*(a+b)
print("length of rectangle", P)
print("perimeter of the rectangle")
c=float(input('side=>'))
d=float(input('side=>'))
P=a+b+c+d
print("perimeter of the rectangle", P)
a=float(input('length of the rectangle=>'))
b=float(input('width of the rectangle=>'))
S=a*b 
print("the area of the rectangle", S)