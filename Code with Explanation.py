import random
#import hashlib

#Set of alphabets, numbers and symbols to choose from it using random module
char = 'qwertyuioplkjhgfdsazxcvbnm,./;[]\\=-098765431QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()'

#input from users
total_pass = int(input("Enter total number of passwords you want : "))
total_char = int(input('How many characters would u like to have : '))

#This for number of passwords You would like to have
for a in range(0,total_pass):
  
    #To store the randomly choosed varibles
    generated_pass = ''
    
    #How many characters to take place in a single password or the length of the password
    for b in range(0,total_char):
      
        #It will choose the characters from the char
        password = random.choice(char)
        
        #It will stores the character in generated_pass
        generated_pass = generated_pass + password
        
    #Final password to print in the console    
    print("The password is : ",generated_pass)

