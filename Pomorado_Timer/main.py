from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
global reps
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    tlabel.config(text='Press Start!', fg=GREEN)
    canvas.itemconfig(timer_text,text='00:00')
    check_mark.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_s = WORK_MIN*60
    break_s = SHORT_BREAK_MIN*60
    if reps%2 != 0:
        tlabel.config(text='Work Time!',fg =RED)
        count(work_s)
    else:
        if reps % 8 == 0:
            tlabel.config(text='Long Break!',fg = PINK)
            count(4*break_s)
        else:
            tlabel.config(text='Break Time!',fg = GREEN)
            count(break_s)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count(c):
        marks = int(c / 60)
        s = int(c % 60)
        if floor(s/10) == 0:
            s = f"0{s}"
        if s == 0:
            s = "00"
        canvas.itemconfig(timer_text, text=f'{marks}:{s}')
        if c > 0:
            global timer
            timer = window.after(1000, count, c-1)
        else:
            start()
            marks=""
            for _ in range(floor(reps/2)):
                marks+='✔'
            check_mark.config(text = marks)

       # print(c)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")



tlabel = Label(text="Timer",font=(FONT_NAME,40,"bold"),bg = YELLOW,fg = GREEN)
tlabel.grid(row=0,column=1)

pic = PhotoImage(file="tomato.png")
canvas = Canvas(width =200,height = 224,bg = YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = pic)
timer_text = canvas.create_text(100,112,text="00:00",fill ='#ffffff',font =(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)


startb = Button(text="Start", command= start)
startb.grid(row=2,column=0)

resetb = Button(text="Reset", command = reset)
resetb.grid(row=2,column=2)

check_mark = Label(text='',fg = GREEN,font = (76),bg = YELLOW)
check_mark.grid(row=3,column=1)

window.config(padx=100,pady=50,bg = YELLOW)
window.mainloop()
