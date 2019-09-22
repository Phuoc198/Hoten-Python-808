while True:
    n = input("Moi ban nhap mat khau: ")
    print(n)
    if len(n) < 8:
        print("Mat khau phai tren 8 ki tu. Moi nhap lai.")
    elif (n.find('0') == -1 and n.find('1') == -1 and n.find('2') == -1 and 
        n.find('3') == -1 and n.find('4') == -1 and n.find('5') == -1 and 
        n.find('6') == -1 and n.find('7') == -1 and n.find('8') == -1 and 
        n.find('9') == -1):
        print("Khong co so. Moi nhap lai")
    else:
        print("Mat khau OK.")
        break