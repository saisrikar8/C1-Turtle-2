'''
03/25/2021
Review

1. import turtle library
  import turtle # Top of page

2. Create a pen/turtle
  variable1 = turtle.Turtle()

3. (Optional) Create a Screen/page
  variable2 = turtle.Screen()

4. Movements

  a. forward
    variable1.fd(DISTANCE)
    variable1.forward(DISTANCE)

  b. backward
    variable1.backward(DISTANCE)
    variable1.bk(DISTANCE)
  
  c. turn right
    variable1.right(ANGLE)
  
  d. turn left
    variable1.left(ANGLE)
  
  e. pen up
    variable1.penup()
  
  f. pen down
    variable1.pendown()
  
  g. move back to (0,0) facing right
    variable1.home()
  
  h. go to a specific point
    variable1.goto(X,Y)

  # Draw a letter
import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
paper.bgcolor("YeLlOW")
pen.color(191970)

pen.speed(10)
pen.width(4)
pen.left(90)
pen.fd(400)
pen.left(90)
pen.fd(80)
pen.bk(160)
pen.penup()
pen.home()
pen.pendown()
pen.fd(80)
pen.bk(160)
  

#SUPER COOL!
import turtle

pen = turtle.Turtle()
pen.speed(10000)
colors = ["royal blue", "red", "dark orange", "purple", "grey", "tan", "burlywood", "light coral"]
length = 10
index = 0
count = 0
for i in range(805):
  pen.color(colors[index])
  pen.forward(length)
  pen.left(130)
  length += 1
  index += 1
  print(count)
  count += 1
  if (index == 7):
    index = 0
'''
import turtle

pen = turtle.Turtle()
pen.speed(10000)
colors = ["royal blue", "red", "dark orange", "purple", "grey", "tan", "burlywood", "light coral"]

angle = 0
index = 0
while(angle < 360):
  pen.color(colors[index])
  index += 1

  if (index == 7):
    index = 0

  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.fd(100)
  pen.left(90)
  pen.home()
  angle += 1
  pen.left(angle)




'''
1. Change turtle speed (0 ~ 10)
  variable1.speed(SPEED)

2. Change width of line
  variable1.width(SIZE)

3. Change color of pen and background
  a. pen color
    variable1.color(COLOR)
  
  b. background color
    variable2.bgcolor(COLOR)

#Draw a circle
  for i in range(360):
    variable1.fd(SIZE)
    variable1.right(1)


'''