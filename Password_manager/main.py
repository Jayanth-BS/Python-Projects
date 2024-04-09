
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
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
def find_password():
    website = web_text.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

def save():

    website = web_text.get()
    email = email_text.get()
    password = pass_text.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_text.delete(0, END)
            pass_text.delete(0, END)
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

get = Button(text="Search", command= find_password)
get.grid(row=1,column=3)

add = Button(text = "Add",width = 36, command = save)
add.grid(row=4,column=1, columnspan=2)

window.config(padx= 50,pady=50)
window.mainloop()