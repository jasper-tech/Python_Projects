#Personal income tax

#Defining variables
income = float(input("Enter the annual income:"))
fixed_amount = 85528
#Using if-else for tax relief calculation
if income <= fixed_amount:
    tax = (18/100*income)-556.2
    tax = round(tax,0)
    print(" Your Tax relief is", tax)
else :
    tax = (income - fixed_amount)*0.32 + 14839.02
    tax = round(tax,0)
    print (" Your Tax relief is",tax)
    
