#Personal income tax


income = float(input("Enter the annual income:"))
fixed_amount = 85528

if income <= fixed_amount:
    tax = (18/100*income)-556.2
    tax = round(tax,0)
    print("Tax relief is", tax)
else :
    tax = (income - fixed_amount)*0.32 + 14839.02
    tax = round(tax,0)
    print ("Tax relief is",tax)
    
