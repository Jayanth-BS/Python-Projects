import random
import hangman_art
import word_book
from replit import clear

print("Welcome to ")
print(hangman_art.logo[0])

word = random.choice(word_book.tech_words)
word = word.lower()

# rand  = random.randint(0,len(words)-1)
# word = words[rand]
# print("Word="+word)

list = []
f=0
life =7
for _ in range(len(word)):
    list += '_'
while life != 0 and list.count('_')!=0:
    guess = input("Guess a letter").lower()
    clear()
    f=0
    if guess in list:
        print(f"You already Guessed the letter {guess}")
    for i in range(0,len(word)):
        if word[i] == guess:
            list[i] = word[i]
            f=1
    if f==0:
        print(f"You guessed a letter {guess} that is not in the word so you loose a life")
        life-=1
    print(hangman_art.pic[7-life]);
    print(list)

if '_' not in list:
    print("You win")
else:
    print("You Lose")
    print("Word is:" + word)
