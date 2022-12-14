#This is a game where the player must guess the states on the US map. Each time the Player guesses a correct state it will appear on the map
import turtle
import pandas

#Initializing the screen using turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Reading CSV data using pandas, converting the states into a list
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
guessed_states = []

#Main game functionality, will run untill the user guesses all 50 states
#Game will check if the answer a user provides exists in a list of states extracted from a CSV file
#If player guesses correctly a turtle object will write the name of the state on the map and add their score to a list of correctly guessed states. 
#Game will generate a CSV file of all the states not guessed if user decides to leave the game early
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if user_answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_answer in state_list:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)
        print("Good Job")
