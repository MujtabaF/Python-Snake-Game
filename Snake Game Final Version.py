import turtle
import time
import random

#Defining the movements
def moveLeft ():
  global direction
  if direction != 'r':
      direction = 'l'
    
def moveRight ():
  global direction
  if direction != 'l':
      direction = 'r'
    
def moveUp ():
  global direction
  if direction != 'd':
      direction = 'u'
    
def moveDown ():
  global direction
  if direction != 'u':
      direction = 'd'

#Setting Up    
wn = turtle.Screen () 
wn.setup(width=600, height=600)
wn.tracer (5)
head = turtle.Turtle ()
head.penup ()
head.color('#2DA7E4')
head.shape ("square")
head.speed (3)
head.shapesize(stretch_wid = 0.9, stretch_len = 0.9)

food = turtle.Turtle ()
food.penup ()
food.color ('purple')
food.shape ('circle')
foodx = random.randint (-14, 14)
foody = random.randint (-14, 14)
food.goto (foodx *20, foody*20)
food.shapesize(stretch_wid = 0.9, stretch_len = 0.9)

wn.listen()

wn.onkeypress (moveLeft, "Left")
wn.onkeypress (moveUp, "Up")
wn.onkeypress (moveDown, "Down")
wn.onkeypress (moveRight, "Right")

direction = "r"

snake = []
snake.append(head)

#Creating a list for the points
grid_points = []

yval = 280
while len(grid_points) < 841:
    xval = -280
    while xval <= 280:
        grid_points.append([xval, yval])
        xval += 20
    yval = yval - 20

#Creating Obstacles
ObList = []
obcount = 0
obindex = 0
while obcount < 10 and grid_points != [[0,0]]:
    o = turtle.Turtle()
    o.penup()
    o.color('red')
    o.shape('square')
    obindex = random.randint(0, len(grid_points))
    o.goto(grid_points[obindex][0], grid_points[obindex][1])
    del grid_points [obindex]
    obcount += 1
    ObList.append([o.xcor(),o.ycor()])
    

count = 0
while True:
    
    wn.update ()
    time.sleep(0.08)

    if abs(head.xcor() - food.xcor()) < 1 and abs(head.ycor() - food.ycor()) < 1: #Checking if there is contact between the head and the food
        newSeg = turtle.Turtle()
        newSeg.shape('square')
        newSeg.shapesize(stretch_wid = 0.9, stretch_len = 0.9)
        newSeg.penup()
        snake.append(newSeg)
        count += 1
        print(count)
        foodx = random.randint (-14, 14)
        foody = random.randint (-14, 14)
        d = 0
        while d < len(snake): #Ensuring that the food doesn't come on the snake body
            if (foodx*20, foody*20) == (snake[d].xcor(), snake[d].ycor()):
                foodx = random.randint (-14, 14)
                foody = random.randint (-14, 14)
            d += 1
            while ([foodx*20, foody*20]) in ObList:
                foodx = random.randint (-14, 14)
                foody = random.randint (-14, 14)
            food.goto(foodx*20, foody*20)
        

    i = len(snake) - 1
    while i > 0:
        snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
        i = i - 1    

    if direction == "r":
        head.setx (head.xcor() + 20)
    elif direction == "l":
        head.setx (head.xcor() - 20)
    elif direction == "u":
        head.sety (head.ycor() + 20)
    elif direction == "d":
        head.sety (head.ycor() - 20)


#Checking for collisions
    a = 1
    while a < len(snake):
        if (head.xcor(), head.ycor()) == (snake[a].xcor(), snake[a].ycor()):
            print("EndGame")
            exit()
        a += 1


    if ([head.xcor(), head.ycor()]) in ObList:
        print("EndGame")
        exit()


    x = int(head.xcor ())
    y = int(head.ycor ())
    if x > (300):
        head.setx (-300)
    if x < (-300):
        head.setx (300)
    if y > (300):
        head.sety (-300)
    if y < (-300):
        head.sety (300)