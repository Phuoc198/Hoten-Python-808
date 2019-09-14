while True:
    n = input("Moi ban nhap mat khau: ")
    print(n)
    if n.isalpha():
        print("mat khau co chua chu")
        break
    
    elif n.isdigit():
        print("mat khau co so")
        break
    else:
        print("mat khau co chua chu va so ")
        