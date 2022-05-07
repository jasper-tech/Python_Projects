#List your variables ie. hour,minutes,duration
hour = int(input("Starting time (hours) :"))
minutes = int(input("Starting time (minutes) :"))
duration = int(input("Event duration (minutes):"))


#Conversion of time
time =  minutes +duration
# if or else for cut and dug conversions
if time > 60:
    cut=((time//60)+hour)%24
    dug=duration+minutes % 60
    
    print(cut,":",dug)
   
    
else:
    print(hour,":",time)
