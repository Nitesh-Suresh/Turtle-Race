"""
Turtle Race
"""

from asyncore import write
from operator import truediv
import turtle, random
r = turtle.Turtle()
r.speed(1)

x=300
y=270
n=int(input("Enter the number players: "))

listofnames=[]
list_players=[]


#1 Draw a play ground
def draw_playground():
    r.pensize(5)
    r.pencolor("blue")
    #r.begin_fill()
    r.penup()
    r.goto(-x,-x)
    r.pendown()
    r.forward(x*2)
    r.left(90)
    r.forward(y*2)
    r.left(90)
    r.forward(x*2)
    r.left(90)
    r.forward(y*2)
    r.left(90)
    #r.end_fill()

#2 Display the title
def print_title():
    r.penup()
    r.goto(0,y)
    r.pendown

    r.pencolor("Green")


    r.write(
        "T U R T L E  R A C E",
        align='center',
        font=('Aria',30,'bold'))


#3 Display Start and Draw a start line
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


#4 Display finish line amd draw a finish line
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

#5 Create a list of 8 turtle and place it before start line

def createplayers():
    gap=0
    for i in range(n):
        print("Enter the name of person",i+1)
        name=input()
        listofnames.append(name)
        t=turtle.Turtle()
        t.shape("turtle")
        t.penup()
        t.goto(-260,160-gap)
        gap=gap+40
        t.write(listofnames[i], align='right', font=("Courier New",8,"bold"))
        t.forward(10)
        t.pendown()
        list_players.append(t)



#6 make all the turtle move towards finish line using random module
#7 Check if the turtle has reached finish line
#8. Display the winner
def start_the_race():
    foundwinner=False
    low=0
    high=5
    while(True):
        for i in range(n):
            list_players[i].forward(random.randint(low,high))

            if list_players[i].xcor()>230:
                winner_index=i
                foundwinner=True
                break

        if foundwinner:
            r.penup()
            r.goto(0,0)
            r.pendown()
            s = listofnames[winner_index] + ' is the winner'
            r.write(s, align='center',font=('Courier New',20,'bold'))
            break
        

draw_playground()
print_title()
start_line()
finish_line()
createplayers()
start_the_race()
