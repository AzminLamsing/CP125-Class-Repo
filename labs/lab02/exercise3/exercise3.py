# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    # TODO: Implement this function
    # Return True if valid, False otherwise
    if(name == "Director" and pin == 1122 ):
        message = True
    elif(name == "Security" and pin == 9900):
        message = True
    else:
        message = False
         
    return message

