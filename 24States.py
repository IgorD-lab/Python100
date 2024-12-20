import pandas
import turtle
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "resources/StatesGame/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

## GET COORDINATES OF THE MOUSE CLICK
# def get_mouse_click_coor(x, y):
#     print(x, y)    
# turtle.onscreenclick(get_mouse_click_coor)
guessed_states = []

state_dict = pandas.read_csv("resources/StatesGame/50_states.csv")

while len(guessed_states) < 50:
    screen.title
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="What's another state's name?").title()
    
    if answer_state == "exit" or "quit" or "cancel" or "q" or "leave":
        missing_states = [state for state in state_dict.state if state not in guessed_states]
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("resources/StatesGame/missing_states.csv")
        break
    
    if answer_state in state_dict.values:
        guessed_states.append(answer_state)                
        state_row = state_dict[state_dict.state == answer_state]
        state_name = state_row.state.item()
        state_x = state_row.x.item()
        state_y = state_row.y.item()
        # print(state_name, state_x, state_y)
        state_label = turtle.Turtle()
        state_label.penup()
        state_label.hideturtle()
        state_label.goto(state_x, state_y)
        state_label.write(state_name)


turtle.mainloop()

