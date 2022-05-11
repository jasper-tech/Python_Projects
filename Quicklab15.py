secret_number = 55

print(
"""
+=====================================+
| Welcome to my game,muggle!          |
| Enter an integer number             |
| And guess what number               | 
|   i've picked for you,              |
|                                     |
| So what is the secret number?       |                           
|                                     |
|                                     |
|                                     |
|                                     |
+=====================================+      

""" )




while True:
    number = int(input("Enter A number:"))
    if number == secret_number:
        print("You're free Comrade hahahaha!!")
        break
    else:
        ("You're Stuck in my loop comrade!!")
        
 
    
