x = int(input("Hay nhap thang: "))

if (x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
    print("Thang",x, "co 31 ngay")

elif (x==4 or x==6 or x==9 or x==11):
    print("Thang" ,x, " co 30 ngay")

else:
    print("Thang 2 co 28 hoac 29 ngay")