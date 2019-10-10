items = ['Rap','Rock','Drum']
print(items)

new_items = input("Nhap ten khac: ")

items.append(new_items)

print(*items, sep='| ')

print(items[0].upper(), items[-1].upper(), items[-2].upper())



