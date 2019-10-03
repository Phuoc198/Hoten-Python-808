x = input("Moi ban nhap day so cach nhau= ")

x1=x.split(",")
for i,item in enumerate(x1):
    if int(item)%2==0:
        print(item)
