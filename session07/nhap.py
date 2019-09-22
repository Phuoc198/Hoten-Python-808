x = input("Moi ban nhap ten dang nhap: ")
print(x)

while True:
    y = input("Moi ban nhap mat khau: ")
    y1 = input("Moi ban nhap lai mat khau: ")
    if y != y1:
        print("Mat khau khong trung khop. Moi nhap lai. ")
    
    elif len(y)<8:
        print("Mat khau toi thieu 8 ki tu. Moi ban nhap lai.")

    elif not (any(c.isdigit() for c in y)):
        print("Mat khau phai chua it nhat 1 chu so. Moi nhap lai")

    elif not (any(b.isalpha() for b in y )):
        print("Mat khau chua it nhat 1 chu cai. Moi nhap lai")

    else:
        break


print(y)

while True:

    z= input("Moi ban nhap email: ")

    if  (z.find('@') == -1):
        print("Email sai moi nhap lai.")

    elif (z.find('.') == -1):
        print("Email thieu dau . VUI LONG NHAP LAI")

    else:
        break





print(z)


