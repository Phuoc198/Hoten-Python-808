while True:
    txt = input("Enter a number: ")
    print(txt)
    if txt.isdigit():
        print("a number")
        break
    else:
        print("not a number")