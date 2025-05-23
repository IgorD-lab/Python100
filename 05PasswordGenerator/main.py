import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for i in range(nr_letters):
    password += letters[random.choice(letters)]
for i in range(nr_symbols):
    password += symbols[random.choice(symbols)]
for i in range(nr_numbers):
    password += numbers[random.choice(numbers)]
    
print(password)


#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
password = ""

for i in range(nr_letters):
    password_list += letters[random.choice(letters)]
for i in range(nr_symbols):
    password_list += symbols[random.choice(symbols)]
for i in range(nr_numbers):
    password_list += numbers[random.choice(numbers)]
    
random.shuffle(password_list)
for char in password_list:
    password += char
    
print(password)