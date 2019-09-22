items = ['phuoc','nam','chi']
print(items)

new_items = input("Nhap ten khac: ")

items.append(new_items)

print(*items, sep=', ')