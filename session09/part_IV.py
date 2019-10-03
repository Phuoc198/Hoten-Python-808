items = [2,32,55,65,12]
Tongchan = 0
Tongle = 0
for i,item in enumerate(items):
    if item %2==0:
        Tongchan += item
        print(i,item)
    else:
        Tongle += item

print("Tong chan la:",Tongchan)
print("Tong le la:",Tongle)
