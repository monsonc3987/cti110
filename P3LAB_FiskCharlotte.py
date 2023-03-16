y = int(input(""))


if y % 4 == 0:

    if y % 100 == 0:
       
        if y % 400 == 0:
           
            print(y, "- leap year")
        else:
           
            print(y, "- not a leap year")
    else:

        print(y, "- leap year")
else:

    print(y, "- not a leap year")
