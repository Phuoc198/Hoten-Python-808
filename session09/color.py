

items = ['vang','xanh','do','tim']
print(*items,sep=' ')

x = input("Moi ban nhap them mau: ")
items.append(x)
print(*items, sep=' ')

#Viết chương trình chứa 1 list chứa ít nhất 3 string đại diện cho 3 màu
y =int(input("Moi ban nhap vi tri: "))
print("Mau o vi tri",y ,"la: ",items[y-1])
print(items)
#Sử dụng list ở bài 1, viết chương trình hỏi người dùng muốn xoá màu nào trong danh sách, nếu người dùng nhập số,
# tự động thực hiện xoá theo vị trí, nếu người dùng nhập chữ, tự động thực hiện xoá theo nội dung

z = input("Ban muon xoa mau nao: ")
if z.isdigit():
    z1 = int(z)
    items.pop(z1)
    print(items)

else:
    for i,item in enumerate(items):
        if item == z:
            items.pop(i)
            break
    print(items)



    
