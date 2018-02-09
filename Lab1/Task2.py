month = int(input("Enter Month\t"))

if 0 < month < 13:
    if month < 4:
        print("Summer")
    elif month < 7:
        print("Autumn")
    elif month < 10:
        print("Spring")
    else:
        print("Winter")
else:
    print("Enter Valid Month")