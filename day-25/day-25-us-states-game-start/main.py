import turtle
from turtle import Turtle,Screen
import pandas


screen=turtle.Screen()

screen.title("US States Game")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
correct_guess=[]
while len(correct_guess) < 50:
    user_state = screen.textinput(f"{len(correct_guess)}/50 States Correct", "What's another state name?").strip().title()
    if user_state == "Exit":
            break
    state_data=pandas.read_csv("50_states.csv")
    matched_state=state_data[state_data["state"]==user_state]

    if not matched_state.empty and user_state not in correct_guess:
        #append correct guess
        correct_guess.append(user_state)
        x=matched_state.iloc[0]["x"]
        y=matched_state.iloc[0]["y"]
        print(x,y)
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x, y)
        writer.write(user_state, align="center", font=("Arial", 10, "normal"))
    else:
        print("Not a valid state")


    missed_states = state_data[~state_data["state"].isin(correct_guess)]
    missed_states.to_csv("states_to_learn.csv", index=False)

    print(missed_states)

screen.mainloop()
