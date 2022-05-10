year = int(input("Enter A Year:"))


if year % 4 != 0:
    print("common year")
elif year % 100 !=0:
    print ("leap year")
elif year % 400!=0:
    print("common year")
elif year < 1582:
    print("Not within the Gregorian calender period")
else:
    print("leap year")
        
