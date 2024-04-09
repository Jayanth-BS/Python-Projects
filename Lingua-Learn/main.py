from tkinter import *
import pandas as pd
import random

words = {}
word = {}

try:
    data = pd.read_csv('data/Words_to_learn.csv')
except FileNotFoundError:
    org_data = pd.read_csv('data/french_words.csv')
    words = org_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

def translate():
    canvas.itemconfig(img, image= white)
    canvas.itemconfig(w, text=word['English'], fill = 'black')
    canvas.itemconfig(lang, text="English",fill = 'black')

def next():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words)
    canvas.itemconfig(img, image=pic)
    canvas.itemconfig(w,text=word['French'], fill = "white")
    canvas.itemconfig(lang,text = "French",fill = "white")
    flip_timer = window.after(3000, translate)

def is_known():

    words.remove(word)
    data = pd.DataFrame(words)
    data.to_csv("data/Words_to_learn.csv", index=False)
    next()

window = Tk()
window.title("Flashy")

flip_timer = window.after(3000, func=translate)

pic = PhotoImage(file ="images/card_back.png")
white = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800,height=526,bg= BACKGROUND_COLOR, highlightthickness=0,)
img = canvas.create_image(400,263,image = pic)
lang = canvas.create_text(400,150,text = "",font = ("Ariel",40,"italic"))
w = canvas.create_text(400,263,text = "",font = ("Ariel",68,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross = PhotoImage(file="images/wrong.png")
cross_img = Button(image=cross, highlightthickness=0, command=next)
cross_img.grid(row=1,column=0)

tick = PhotoImage(file ="images/right.png")
tick_img = Button(image = tick, highlightthickness=0, command= is_known)
tick_img.grid(row=1,column=1)

next()

window.config(bg=BACKGROUND_COLOR, padx=40,pady=40)
window.mainloop()
