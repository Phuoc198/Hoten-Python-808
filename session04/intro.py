yob = int(input("Your year of birth: "))
age = 2019 - yob
print (age)

if age < 10:
    print("baby")

elif age < 18:
    print("teenager")
else:
    print("adult")