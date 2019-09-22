
y =int(input("Moi nhap so canh: "))
x =((y-2)*180)/y
a = 1
from turtle import *
speed(-1)
shape("turtle")
color("red")

while a<=y:
    forward(100)
    left(180-x)
    a+=1

mainloop()

