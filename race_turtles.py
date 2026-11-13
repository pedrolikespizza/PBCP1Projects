import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race!")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create the finish line
finish_line = 300

line = turtle.Turtle()
line.penup()
line.goto(finish_line, 250)
line.pendown()
line.right(90)
line.forward(500)
line.hideturtle()

# List of turtle colors
colors = ["red", "blue", "green", "yellow", "purple"]

# Create the racing turtles
turtles = []

starting_y = 150

for color in colors:
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-350, starting_y)
    turtles.append(racer)

    starting_y -= 75

# Race the turtles
winner = None

while winner is None:
    for racer in turtles:
        # Move a random number of steps
        steps = random.randint(1, 10)
        racer.forward(steps)

        # Check if the turtle crossed the finish line
        if racer.xcor() >= finish_line:
            winner = racer.pencolor()
            break

# Announce the winner
print("The " + winner + " turtle won the race!")

# Display winner on the turtle screen
announcement = turtle.Turtle()
announcement.hideturtle()
announcement.penup()
announcement.goto(0, -220)
announcement.write(
    "The " + winner + " turtle won!",
    align="center",
    font=("Arial", 24, "bold")
)

# Keep the window open
screen.mainloop()