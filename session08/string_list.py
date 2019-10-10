# print("Viết một chương trình thực hiện việc nhập nhiều hơn 1 sở thích trong cùng 1 lần, các sở thích cách nhau bởi dấu ‘,’")
# x = input("Moi nhap vao cac so thich cua ban: ")

# print(x)
# x1=x.split(",")
# print(x1)

# for i,item in enumerate(x1):
#     print(i+1,".",item.upper())


# print("Viết một chương trình thực hiện việc trộn các chữ cái trong 1 từ do người dùng nhập vào")

# import random

# x2 = input("Moi ban nhap: ")

# n = list(x2)

# random.shuffle(n)



# for i in n:
#     print(i)



print("Viết một chương trình chọn 1 từ ngẫu nhiên từ trong 1 danh sách từ có trước, trộn các chữ cái của từ này rồi in ra (trên cùng một dòng) để người chơi đoán. Sau khi người chơi nhập vào, so sánh với từ gốc và in ra kết quả đúng sai")


import random
items = ['Cho','Meo','Ga','Lon']

index = random.randint(0, 3)

newList = list(items[index])
random.shuffle(newList)

for i in newList: 
    print(i)

answer = input("Moi ban doan : ")
if answer == items[index]:
    print("Ban da doan dung")
else: 
    print("Ban da doan sai")


