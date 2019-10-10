items=['Hoat hinh' , 'Kinh di', 'Hai huoc', 'Hanh dong','Kiem hiep','Co trang','Trinh tham']

items[1] ='Lang man'
print(items)
items[-1] = 'Dragon ball'
print(items)

# update gia tri phan tu vi tri x
x = int(input("Moi nhap vao vi tri item : "))
print(x)
y = input("Moi nhap vao gia tri item : ")
print(y)
items[x] = y
print(items)

# Xoá phần tử thứ hai trong list của bài tập trước
items.pop(1)
print(items)

# Xoá phần từ có nội dung ‘Hai huoc’ trong bài tậptrước, nếu phần tử này không tồn tại, cần kiểm tra và báo lại
f=bool(False)
for i,item in enumerate(items):
    if(item == 'Hai huoc'): 
        items.pop(i)
        f = True

if f == False:
    print("Khong co phan tu 'Hai huoc '")

print(items)

# Xoá một phần tử bất kỳ trong list của bài trước, vị trí của phần tử này do người dùng nhập vào
x1 = int(input("Moi ban nhap vao vi tri can xoa: "))
items.pop(x1)
print(items)


# Xoá một phần tử bất kỳ trong list ở bài trước , giá trị của phần tử này do người dùng nhập vào
x2= input("Moi nhap vao gia tri can xoa: ")

f1=bool(False)
for i,item in enumerate(items):
    if(item == x2): 
        items.pop(i)
        f1 = True

if f1 == False:
    print("Khong co phan tu: ",x2)

print(items)

