items = ['cho','meo','lon','ga','trau']

print('Thêm 3 sở thích mới vào cho list bài trước , sau đó in ra mỗi phần tử này một dòng')
for i,item in enumerate(items):
    print(i+1,".",item)

print('In ra list của bài tập trước mỗi phần tử này một dòng, các phần tử này phải được in hoa')
for i,item in enumerate(items):
    print(item.upper())

print("In ra list của bài tập trước mỗi phần tử này một dòng, các phần tử này phải được in hoa và được đánh số thứ tự")

for i,item in enumerate(items):
    print(i+1,".",item.upper())

print("In ra list của bài tập trước mỗi phần tử này một dòng, chỉ in ra các phần tử có chứa chữ 'e' hoặc 'E' :")

for i,item in enumerate(items):
    if (item.find('e') != -1 or item.find('E') != -1):
        print(i+1,".",item)


