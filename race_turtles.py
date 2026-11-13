#pb period 2 turtle racing

import turtle as t

import random


t.showturtle()


finish = t.Turtle()
finish.right(90)
finish.teleport(500,500)
finish.forward(1000)


red = t.Turtle()
red.penup()
red.shape("turtle")
red.forward(100)
red.color("red")
red.goto(100,100)
red.pendown()


blue = t.Turtle()
blue.penup()
blue.shape("turtle")
blue.forward(200)
blue.color("blue")
blue.goto(100,200)
blue.pendown()




green = t.Turtle()
green.penup()
green.shape("turtle")
green.forward(300)
green.color("green")
green.goto(100,300)
green.pendown()





purple = t.Turtle()
purple.penup()
purple.shape("turtle")
purple.forward(100)
purple.color("purple")
purple.goto(100,400)
purple.pendown()



yellow = t.Turtle()
yellow.penup()
yellow.shape("turtle")
yellow.forward(100)
yellow.color("yellow")
yellow.goto(100,500)
yellow.pendown()













t.done()


