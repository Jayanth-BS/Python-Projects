import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j ','l', 'm', 'n', 'o', 'q', 'r', 's', 't', 'U' 'p', 'q', 'y', 'z', 'A', 'B', 'C', 'D',' i', 'j', 'k', 'u', 'v', 'w', 'x', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'E'
'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")
l = int(input("Enter the no of letters"))
d = int(input("Enter the no of digits"))
s = int(input("Enter the no of symbols"))

k=""
for i in range(0,l):
    rand_l = random.randint(0,25)
    k += letters[rand_l]
for i in range(0,d):
    rand_l = random.randint(0,9)
    k += numbers[rand_l]
for i in range(0,s):
    rand_l = random.randint(0,8)
    k += symbols[rand_l]

print(f"Generated Password:{''.join(random.sample(k,len(k)))}")
