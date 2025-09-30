# main.py

# Import necessary libraries
import turtle  # For creating the game window and drawing
import pandas  # For reading and handling data from the CSV file

# --- Screen Setup ---
# Create a screen object, which is the main window for the game
screen = turtle.Screen()
screen.title("U.S. States Game")  # Set the title of the window

# Define the path to the background image
image = "blank_states_img.gif"
# Register the image as a new shape that the turtle can use
screen.addshape(image)
# Change the turtle's shape to the map image, making it the background
turtle.shape(image)

# --- Data Loading and Initialization ---
# Read the state coordinates from the CSV file into a pandas DataFrame
data = pandas.read_csv("50_states.csv")
# Create a list of all state names from the 'state' column of the DataFrame
all_states = data.state.to_list()
# Initialize an empty list to store the names of states the user has guessed correctly
guessed_states = []

# --- Main Game Loop ---
# The loop continues as long as the user has not guessed all 50 states
while len(guessed_states) < 50:
    # Prompt the user with a pop-up input box
    # The title of the box shows the current score (e.g., "15/50 States Correct")
    # .title() capitalizes the user's input (e.g., "new york" -> "New York") to match the data
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # --- Exit Condition ---
    # Allow the user to exit the game by typing "Exit"
    if answer_state == "Exit":
        # --- IMPROVEMENT: Using a list comprehension ---
        # This single line does the same job as the original for loop.
        # It creates a new list 'missing_states' containing every 'state' from 'all_states'
        # if that 'state' is not found in the 'guessed_states' list.
        missing_states = [state for state in all_states if state not in guessed_states]

        # Create a new DataFrame from the list of states the user missed
        new_data = pandas.DataFrame(missing_states)
        # Save this DataFrame to a new CSV file for the user to study
        new_data.to_csv("states_to_learn.csv")
        # Exit the while loop, which ends the game
        break

    # --- Check if the Guess is Correct ---
    # Check if the user's answer is one of the states in the master list
    if answer_state in all_states:
        # Add the correct guess to the list of guessed states
        guessed_states.append(answer_state)
        # Create a new turtle object to write the state name on the map
        t = turtle.Turtle()
        t.hideturtle()  # Make the turtle icon invisible
        t.penup()  # Lift the "pen" so it doesn't draw a line when it moves

        # Get the row from the DataFrame where the state name matches the user's answer
        state_data = data[data.state == answer_state]
        # Move the turtle to the x and y coordinates for that state
        # .item() gets the single value from the pandas Series
        t.goto(int(state_data.x), int(state_data.y))
        # Write the state's name at that position
        t.write(answer_state)

# (Optional) You can add a turtle.mainloop() or screen.exitonclick() at the end
# if you want the window to stay open after the game is won, but it's not necessary
# for the core logic.