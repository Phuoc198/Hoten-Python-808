items = [45, 67, 56, 78,42,61,43]
for i,item in enumerate(items):
    print(i,", ",item)

x = int(input("Nhap diem moi: "))
items.append(x)

for i,item in enumerate(items):
    print(i,", ",item)

print("sap sep lai:")
items.sort(reverse=True)
for i,item in enumerate(items):
    print(i,", ",item)

print("5 nguoi cao nhat: ")

for i,item in enumerate(items):
    if i<5:
        print(i,", ",item)
    