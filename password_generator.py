import random
import hashlib

char = 'qwertyuioplkjhgfdsazxcvbnm,./;[]\\=-098765431QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()'
total_pass = int(input("Enter total number of passwords you want : "))
total_char = int(input('How many characters would u like to have : '))
for a in range(0,total_pass):
    generated_pass = ''
    for b in range(0,total_char):
        password = random.choice(char)
        generated_pass = generated_pass + password
    print("The password is : ",generated_pass)






























