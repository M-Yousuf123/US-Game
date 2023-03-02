import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


def write_name(state_data):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(int(state_data.x), int(state_data.y))
    new_turtle.write(f"{state_data.state.item()}", False, "center", ('Arial', 8, 'normal'))


game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    guess_state = answer_state.title()
    get_state = data[data.state == guess_state]
    if not get_state.empty:
        score += 1
        write_name(get_state)

turtle.mainloop()

# This below code can be used to get the coordinates of the states as we click on it
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
