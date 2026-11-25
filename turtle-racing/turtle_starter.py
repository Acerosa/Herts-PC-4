"""Turtle Racing Game: guided coding starter.

Run this file first. The window and two turtles are already prepared.
During the lesson, add the game features in the sections marked .

Assignment 2 links: random numbers, loops, comparisons, lives,
closest result, input validation and replay.
"""

import turtle
import random
import time

# QUICK REFERENCE
# turtle.Screen()          Creates the game window.
# turtle.Turtle()          Creates a turtle we can move or draw with.
# .shape("turtle")         Changes the cursor into a turtle.
# .color("red")           Sets the turtle's colour.
# .penup()                 Moves without drawing a line.
# .pendown()               Draws a line while moving.
# .goto(x, y)              Moves to a position on the screen.
# .setheading(0)           Points right (0 degrees).
# .forward(distance)       Moves forwards by the given distance.
# .xcor()                  Returns the current horizontal position.
# .right(degrees)          Turns clockwise.
# .write(text, ...)        Displays a message on screen.
# .clear()                 Removes text or drawings made by that turtle.
# .hideturtle()            Hides the turtle cursor.
# .pensize(5)              Sets the drawing line thickness.
# window.textinput(...)    Asks for text in a pop-up box; Cancel returns None.
# random.randint(1, 20)   Picks a random whole number from 1 to 20.
# time.sleep(0.05)         Waits briefly so we can see the movement.
# abs(number)              Returns the distance from zero (never negative).
# .strip()                 Removes spaces at the start and end of text.
# .lower()                 Converts text to lowercase.
# .isdigit()               Checks whether a string contains digits only.
# int(text)                Converts valid number text into an integer.

# SCREEN SETUP 
window = turtle.Screen()
window.title("Turtle Racing Game")
window.bgcolor("lightgreen")
window.setup(width=800, height=400)

# RED TURTLE 
red = turtle.Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(-300, 50)

# BLUE TURTLE 


# FINISH LINE 
# The finish line is at x = 250.
finish = turtle.Turtle()
finish.hideturtle()
finish.color("black")
finish.pensize(5)
finish.penup()
finish.goto(250, -150)
finish.pendown()
finish.goto(250, 150)

# MESSAGE DISPLAY 
message = turtle.Turtle()
message.hideturtle()
message.penup()

# RESET THE RACE 
# Later, move this block inside the replay loop.
red.goto(-300, 50)
red.setheading(0)

message.clear()

# Display a message .
message.goto(0, 130)
message.write("Get ready!", align="center", font=("Arial", 24, "bold"))

#  1: Random movement
# Replace the fixed distances below with random.randint(1, 20).
# Store each generated number in a variable before moving the turtle.
# randint includes both endpoints.
# Assignment 2: generate a random secret PIN.
red.forward(10)


# Checkpoint: run several times and observe the movement.

#  2: Racing loop
# Wrap the movement above in a while loop.
# Continue while both x coordinates are below 250.
# Move both turtles once per iteration.
# Use time.sleep(0.05) inside the loop to slow the race.
# Assignment 2: repeat guesses until the game ends.

# Checkpoint: the race stops when at least one turtle reaches the line.

#  3: Determine the winner
# Use if, elif and else to store red, blue or draw in winner.
# A draw occurs if both cross the line in the same iteration.
# Check for a draw before checking individual winners.
# Assignment 2: compare values and select the appropriate outcome.

# Display the result using the example below.
# message.clear()
# message.write(winner, align="center", font=("Arial", 24, "bold"))

# Checkpoint: the displayed result matches the race outcome.

#  4: Predict the winner
# Move the input example below to BEFORE the racing loop.
# textinput returns a string, or None if the player presses Cancel.
# prediction = window.textinput("Predict the Winner", "Red or Blue?")
# Compare prediction with winner AFTER the race.
# Assignment 2: accept and check a player's guess.

# Checkpoint: predict each colour and check the feedback.

#  5: Replay
# Create a variable to control whether another race is played.
# Wrap the reset, prediction, race and result in an outer while loop.
# Ask whether the player wants another race after displaying the result.
# play_again = window.textinput("Play Again", "Race again? (y/n)")
# Assignment 2: restart the game without restarting the program.

# Checkpoint: y starts a fresh race; n ends the game.

#  6: Limited lives
# Initialise lives before the outer loop, starting with 3 for now.
# Subtract one life for an incorrect prediction, but not for a draw.
# Update the outer loop condition to stop when lives reach zero.
# Display the remaining lives and a game over message when appropriate.
# Assignment 2 Stage 1: manage limited attempts.

# Checkpoint: a wrong prediction reduces lives by one.

#  7: Closest losing distance
# When a prediction is wrong, use the chosen turtle's x coordinate.
# abs(250 - position) gives its distance from the finish line.
# Assignment 2 Stage 1: calculate the difference between two numbers.

# Checkpoint: compare the printed distance with the losing position.

#  8: Track the closest result
# Initialise closest_distance to None before the outer loop.
# Store the first losing distance, then replace it only if a smaller
# distance is recorded. Display the best result when the game ends.
# Assignment 2 Stage 1: remember the closest incorrect guess.

# Checkpoint: a larger losing distance must not replace a smaller one.

#  9: Validate the number of lives
# Replace the fixed starting lives with a text input before the outer loop.
# lives_input = window.textinput("Choose Lives", "Choose 1 to 5 lives")
# Check for None before using string methods. Cancel defaults to 3 lives.
# Use .strip() to remove surrounding spaces.
# Use .isdigit() and .isdecimal() to check for decimal digits before int().
# Check the permitted range from 1 to 5 and repeat invalid input.
# Assignment 2 Stage 3: type and range checks.

# Checkpoint: try an empty answer, hello, 0, 6, 2.5 and 3.

#  10: Validate prediction and replay
# Check for None before calling string methods.
# Use .strip().lower() to accept surrounding spaces and capital letters.
# Repeat the question until red or blue (prediction), or y or n (replay).
# Cancel ends the game rather than causing an error.
# Assignment 2 Stage 3: presence and allowed value checks.

# Checkpoint: try empty input, an invalid colour, RED and Cancel.

# OPTIONAL CELEBRATION 
# Move this example inside the outer loop, after displaying the result
# and before asking to replay. Adapt it to the winning turtle.
# for spin in range(12):
#     red.right(30)
#     time.sleep(0.05)

# Keep this at the bottom of the file so the window stays open.
turtle.done()
