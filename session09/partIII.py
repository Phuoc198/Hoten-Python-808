items = [2,5,6,26,76,44]

x = int(input("Enter a number: "))

f = bool(False)

for i,item in enumerate(items):
    if item == x:
        print("Found, position:",i)
        f = True
        break
if(f==False):
    print("Not found in our list")


print("Tong Dung Ham sum() = ",sum(items))

Tong = 0

for i,item in enumerate(items):
    Tong +=item 
    print(i,Tong)

print("Tong ko dumg sum()= ",Tong)
