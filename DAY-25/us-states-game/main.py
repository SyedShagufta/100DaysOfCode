import pandas
import pandas as pd
import turtle

# 1. Convert the guess to Title Case
# 2. Check if the guess is among the 50 states
# 3. Write correct guesses onto the Map
# 4. Use a loop to allow the user to keep guessing
# 5. Record the correct guesses in a list
# 6. Keep track of the course

screen = turtle.Screen()
screen.title("U.S States Game!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's "
                                                                                            "name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_state]
        # for state in states_list:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Learn.csv")
        break
    if answer_state in states_list and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# add remaining states to learn.csv