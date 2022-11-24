#Turtle game using package 'turtle'
#racing of two turtles

#importing necessary modules
import turtle
import random
import time


#setup for screens
screen = turtle.Screen()
screen.bgcolor('lightblue')


#setup for players
player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')

player_two = player_one.clone()
player_two.color('red')


#positioning the players
player_one.penup()
player_one.goto(-300,200)

player_two.penup()
player_two.goto(-300,-200)


#finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write(' FINISH', font=36)


#return to start position
player_one.penup()
player_one.color('blue')
player_one.goto(-300, 200)
player_one.right(90)


#pendown is used to mark the movement
player_one.pendown()
player_two.pendown()

die = [1, 2, 3, 4, 5, 6]


#backend of the racing game
for i in range(30):
    if player_one.pos() >= (300, 250):
        print("Player One Wins the Race")
        break
    elif player_two.pos() >= (300, -250):
        print("Player Two Wins the Race")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
        time.sleep(1)



#after the race is completed, it shows winner name as output
#turtle.done()