ten_quan =['ST','BD','BTG','CG','DD','HBT']
dien_tich = [117.43,9224,43.35,1204,996,1009]
dan_so =[150300,247800,333300,266800,420900,318000]
mat_do =[]

print("Quan co dan so lon nhat: ",max(dan_so))
print("Dan so nho nhat la: ",min(dan_so))

for i,item in enumerate(dan_so):
    if item == max(dan_so):
        print("Ten quan dong dan nhat la: ",i,ten_quan[i])
    if item == min(dan_so):
        print("Ten quan it dan nhat la: ",i,ten_quan[i])

for i,item in enumerate(dan_so):
        md=float(item/dien_tich[i])
        mat_do.append(md)
print(mat_do)

print("Mat do dan cu trung binh: ",sum(mat_do) / len(ten_quan))
        