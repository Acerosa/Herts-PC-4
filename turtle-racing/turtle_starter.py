"""Turtle Racing Game: guided coding starter.

Run this file first. The window and two turtles are already prepared.
During the lesson, add the game features in the sections marked CODE ALONG.

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
# window.textinput(...)    Asks for text in a pop-up box; Cancel returns None.
# random.randint(1, 20)   Picks a random whole number from 1 to 20.
# time.sleep(0.05)         Waits briefly so we can see the movement.
# abs(number)              Returns the distance from zero (never negative).
# .strip()                 Removes spaces at the start and end of text.
# .lower()                 Converts text to lowercase.
# .isdigit()               Checks whether a string contains digits only.
# int(text)                Converts valid number text into an integer.

# SCREEN SETUP (PROVIDED)
window = turtle.Screen()
window.title("Turtle Racing Game")
window.bgcolor("lightgreen")
window.setup(width=800, height=400)

# RED TURTLE (PROVIDED)
red = turtle.Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(-300, 50)

# BLUE TURTLE (PROVIDED)
blue = turtle.Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(-300, -50)

# FINISH LINE (PROVIDED)
# The finish line is at x = 250.
finish = turtle.Turtle()
finish.hideturtle()
finish.color("black")
finish.pensize(5)
finish.penup()
finish.goto(250, -150)
finish.pendown()
finish.goto(250, 150)

# MESSAGE DISPLAY (PROVIDED)
message = turtle.Turtle()
message.hideturtle()
message.penup()

# STARTER DEMO: Run the file and watch both turtles move once.
# CODE ALONG 1: Replace these fixed distances with random.randint(1, 20).
# Assignment 2: generate a random secret PIN using random.randint().
red.forward(10)
blue.forward(15)

# CODE ALONG 2: Build a racing loop.
# Reset the turtles to x = -300 using .goto() before the race.
# Use a while loop to keep both moving until at least one reaches x = 250.
# Use .xcor() to check each turtle's position.
# Tip: Move BOTH turtles once per loop before checking who won.
# Assignment 2: repeat guesses until the game ends.

# CODE ALONG 3: Determine the winner.
# Use if / elif / else to set winner to "red", "blue" or "draw".
# A draw happens when both cross the line in the same movement round.
# Assignment 2: compare a guess with the secret PIN.

# CODE ALONG 4: Ask the player to predict the winner.
# Use window.textinput() to ask for red or blue BEFORE the race.
# Check the prediction against winner AFTER the race.
# Assignment 2: ask for and check the player's guess.
# Teaching note: Move this input section above the racing loop when adding it.

# CODE ALONG 5: Add limited lives.
# Ask the player for 1 to 5 lives before their first race.
# Subtract one life for a wrong prediction; a draw costs no life.
# Assignment 2 Stage 1: limited attempts.

# CODE ALONG 6: Track the closest losing distance.
# When the player predicts incorrectly, use abs() to find how far
# their selected turtle was from the finish line (x = 250).
# Keep the smallest distance across races.
# Assignment 2 Stage 1: track the closest incorrect guess.

# CODE ALONG 7: Validate input.
# For turtle choice, use .strip().lower() and accept only red or blue.
# For lives, use .isdigit(), int() and check the range 1 to 5.
# Check for None BEFORE calling string methods: Cancel returns None.
# Assignment 2 Stage 3: input validation.

# CODE ALONG 8: Add replay and celebration.
# Ask for y or n after each race; validate the answer.
# Reset both turtles to the start and face right with .setheading(0).
# Stop when the player chooses n or has no lives left.
# Optional: celebrate with a for loop and .right(30) twelve times.
# Assignment 2: replay and game state.

# Keep this at the bottom of the file.
turtle.done()
