dic ={
    "name" : "XXXTENTACION",
    "Born" : 1998,
    "description" : "Rapper",
}
print(dic)

del dic["name"]
print(dic)

# Lặp lại bài trước với key muốn xoá được nhập từ người dùng

x = input("Moi nhap key ban muon xoa: ")

for key in dic:
    if key == x:
        del dic[key]
        break
print(dic)