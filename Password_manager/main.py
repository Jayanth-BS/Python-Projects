
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def fill():
    if len(web_text.get())==0 or len(pass_text.get())==0:
        messagebox.showinfo(title="oops", message="Please fill all the fields")
    else:
        f = open("local.txt", "a")
        f.write(f"{web_text.get()} | {email_text.get()} | {pass_text.get()}\n")
        web_text.delete(0,END)
        pass_text.delete(0, END)
        messagebox.showinfo(title="Title",message="Message")
        f.close()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')

pic = PhotoImage(file = "logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image = pic)
canvas.grid(row =0,column=1)

web = Label(text = "Website:")
web.grid(row=1,column=0)

web_text = Entry(width = 35)
web_text.grid(row=1,column=1, columnspan=2)
web_text.focus()

email = Label(text = "Email/Username:")
email.grid(row=2, column=0)

email_text = Entry(width = 35)
email_text.grid(row=2,column=1, columnspan=2)
email_text.insert(0,"jayanthkbs.cs21")
passw = Label(text = "Password:")
passw.grid(row=3, column=0)

pass_text = Entry(width = 35)
pass_text.grid(row=3,column=1,columnspan=2)

get = Button(text="Generate Password", command= generate_password)
get.grid(row=3,column=3)

add = Button(text = "Add",width = 36, command = fill)
add.grid(row=4,column=1, columnspan=2)

window.config(padx= 50,pady=50)
window.mainloop()
