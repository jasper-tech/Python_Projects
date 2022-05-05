hour = int(input("Starting time (hours) :"))
minutes = int(input("Starting time (minutes) :"))
duration = int(input("Event duration (minutes):"))


time =  minutes +duration
if time > 60:
    cut=((time//60)+ hour) % 24
    dug=duration+minutes % 60
    
    print(cut,"::",dug)
   
    
else:
    print(hour,"::",time)
