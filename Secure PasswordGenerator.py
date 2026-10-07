      
#Import Random and String Module

import secrets
import string

#Decide Your Password's Characters and its length

characters = string.ascii_letters + string.digits + string.punctuation

length = 16

#Secure Random Password with Unique Characters

password = "".join(secrets.choice(characters) for _ in range(length))
	
print("Your Secure Password is:",password)


