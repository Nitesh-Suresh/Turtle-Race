"""
Turtle Race
"""

import turtle
import random
import time

# Initialize the turtle
r = turtle.Turtle()
r.speed(1)

# Define constants
x=300
y=270

# Get the number of players from user
n=int(input("Enter the number players: "))

# Lists to store player names and turtle objects
listofnames=[]
list_players=[]
start_times={}


#Function to Draw a play ground
def draw_playground():
    r.pensize(5)
    r.pencolor("gray")
    r.penup()
    r.goto(-x,-x)
    r.pendown()
    for _ in range(2):
        r.forward(x * 2)
        r.left(90)
        r.forward(y * 2)
        r.left(90)

#2 Function to Display the title
def print_title():
    r.penup()
    r.goto(0,y)
    r.pendown()
    r.pencolor("darkblue")
    r.write(
        "T U R T L E  R A C E",
        align='center',
        font=('Arial',30,'bold'))

#3 Function to Display Start and Draw a start line
def start_line():
    r.penup()
    r.goto(-230,180)
    r.pendown()
    r.pencolor("red")
    r.write(
        'START', 
        align="center",
        font=('Times',18,'bold')
    )
    r.goto(-230,-250)


#4 Function to Display finish line amd draw a finish line
def finish_line():
    r.penup()
    r.goto(230,180)
    r.pendown()
    r.pencolor("GREEN")
    r.write(
        'FINISH', 
        align="center",
        font=('Arial',18,'bold')
    )
    r.goto(230,-250)

#5 Function to create players (turtles)
def createplayers():
    gap=0
    for i in range(n):
        name=input("Enter the name of person "+str(i+1)+": ")
        listofnames.append(name)
        t=turtle.Turtle()
        t.shape("turtle")
        t.penup()
        t.goto(-260,160-gap)
        gap+=40
        t.write(
            listofnames[i], 
            align='right', 
            font=("Courier New",8,"bold")
        )
        t.forward(10)
        t.pendown()
        list_players.append(t)



#Function to start the race
def start_the_race():
    foundwinner=False

    for i in range(n):
        start_times[i] = time.time()
    while not foundwinner:
        for i in range(n):
            list_players[i].forward(random.randint(0,5))

            if list_players[i].xcor()>230:
                winner_index=i
                foundwinner=True
                break

    r.penup()
    r.goto(0, 0)
    r.pendown()
    winner_message = listofnames[winner_index] + ' is the winner'
    r.write(
        winner_message, 
        align='center', 
        font=('Courier New', 20, 'bold')
    )

    # Calculate and display time taken by each player
    for i in range(n):
        end_time = time.time()
        time_taken = end_time - start_times[i]
        t = list_players[i]
        t.penup()
        t.goto(-230, t.ycor())
        t.write(
            f'Time: {time_taken:.2f} seconds',
            align='center',
            font=('Arial', 12, 'normal')
        )
        
# Main game logic
draw_playground()
print_title()
start_line()
finish_line()
createplayers()
start_the_race()

# Keep the window open for 7 seconds
time.sleep(7)

# Close the turtle graphics window
turtle.bye()
