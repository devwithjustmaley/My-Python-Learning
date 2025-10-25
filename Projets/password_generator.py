import random
import string

def generator(l):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.punctuation
    numbers = string.digits
    all_characters = lowercase + uppercase + symbols + numbers
    if l < 6:
        print("The password lenght must be over 6")
        return ""
    
    password = []

    for _ in range(l):
        password.append(random.choice(all_characters))
    
    return print("".join(password))


lenght = int(input("Enter the lenght of the password "))
generator(lenght)