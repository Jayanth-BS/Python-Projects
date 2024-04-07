import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
#defining image as the shape
screen.addshape(image)
#giving that shape
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


guessed_state = []
while len(guessed_state)<50:
    ans_state = screen.textinput(title=f'{len(guessed_state)}/50 States Correct', prompt="What's another state's name?").title()
    if ans_state == 'Exit':
        miss = [i for i in all_states if i not in guessed_state]
        df = pandas.DataFrame(miss)
        df.to_csv("States You Missed XD.csv")
        break;
    if ans_state in all_states and ans_state not in guessed_state:
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()         #hides turtle cursor(that arROW)
        t.penup()                            #prevent marking
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(ans_state)

screen.exitonclick()
