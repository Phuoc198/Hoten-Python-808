items = ['Chao','Pho','Com','Bun','Mien']


while True:
    x = list(input("Moi ban nhap thao tac: "))

    if 'C' in x:
        x1 = input("Nhap ten khac: ")

        items.append(x1)
    
        print(*items, sep=' ')
        break

    if 'R' in x:
        for i,items in enumerate(items):
            print(i+1,".",items.upper())
            break

    if 'U' in x:
        x2 = int(input("Moi nhap vao vi tri item : "))
        print(x2)
        y = input("Moi nhap vao gia tri item : ")
        print(y)
        items[x2] = y
        print(items)
        break

    if 'D' in x:
        x3 = int(input("Vi tri ban muon xoa: "))
        items.pop(x3)
        print(items)
        break


    