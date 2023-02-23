import turtle as t
import random

wn = t.Screen()
wn.setup(1000, 1000)
wn.setworldcoordinates(-500, -100, 500, 500)
wn.bgcolor("black")

qwer=t.Turtle()
qwer.speed(0)
qwer.color("white")
qwer.hideturtle()
triSize = 400 # desired height and width of the triangle




def firstPoint():
    qwer.up()
    initX = random.randint(-triSize, triSize)
    #print(initX, ",", triSize - (abs(initX) * 2))
    sumthin = (triSize - (abs(initX))) * 2
    if (sumthin < 0):
        sumthin = -sumthin

    initY = random.randint(0, sumthin)
    qwer.goto(initX, initY)
    qwer.down()
    qwer.dot(4)


firstPoint()
qwer.up()
for i in range(5000):
    givenX = random.choice([-triSize, 0, triSize])
    if givenX == 0:
        givenY = triSize
    else:
        givenY = 0


    newX = ((givenX + qwer.xcor()) / 2)
    newY = ((givenY + qwer.ycor()) / 2)
    
    qwer.goto(newX, newY)
    qwer.dot(4)

    #print(givenX, newX, qwer.xcor())



wn.exitonclick()

