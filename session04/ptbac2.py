import math  

print("Giải phương trình bậc 2: a*x*x + b*x + c = 0")
a = float(input("nhap so a=  "))
b = float(input("nhap so b= "))
c = float(input("nhap so c= "))

D= b*b - 4*a*c

if D < 0:
    print("Delta=",D,". Phương trình vô nghiệm.")

elif D==0: 
    x = -b/(2*a)
    print("Phương trình có nghiệm kép: x=",x)
else:
    x1 = (-b - math.sqrt(D))/(2*a)
    x2 = (-b + math.sqrt(D))/(2*a)
    print("Phương trình có 2 nghiệm phân biệt: ")
    print("x1=",x1)
    print("x2=",x2)
    