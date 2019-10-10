dic ={
    "name" : "XXXTENTACION",
    "Born" : 1998,
    "description" : "Rapper",
}
print(dic)

dic["Sex"] = "Man"
# In ra trường tên (name), và mô tả (description) của dictionary ở bài trước
print(dic["name"],dic["description"])

# Lặp lại bài trước với key nhập từ bàn phím


x =input("Moi ban nhap key: ")
y = input("Moi ban nhap value: ")
# x1 =input("Moi ban nhap key2: ")
# y1 =input("Moi ban nhap value2: ")
# x2 =input("Moi ban nhap key3: ")
# y2 =input("Moi ban nhap value3: ")
dic[x] = y

# dic[x1] = y1
# dic[x2] = y2

print(dic)