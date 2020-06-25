import turtle
from random import randint, random

MINIMUM_BRANCH_LENGTH = 5
count = 0

def build_tree(t, branch_length, shorten_by, angle, level):
  if branch_length > MINIMUM_BRANCH_LENGTH:
    global count
    count = count +1
	
    if(level < 2):
      color = "black"
      pensz = 3
    else:
      if(randint(0,9)%8 == 0 and  branch_length > (MINIMUM_BRANCH_LENGTH * 4)):
        color = "black"
        pensz = 2
      else:
        color = "#CC00CC"
        pensz = 1

    t.color(color)
    t.pensize(pensz)
    t.forward(branch_length)
    new_length = branch_length - shorten_by

    theta = randint(10,20)
    density = branch_length * random()

    t.left(angle)
    build_tree(t, new_length, shorten_by, angle, level + 1)
    if(density > MINIMUM_BRANCH_LENGTH):
       build_tree(t, new_length, 10, theta, level + 1)

    t.right(angle * 2)
    build_tree(t, new_length, shorten_by, angle, level + 1)
    if(density > MINIMUM_BRANCH_LENGTH):
       build_tree(t, new_length, 10, theta, level + 1)

    t.left(angle)
    
    t.color(color)
    t.pensize(pensz)
    t.backward(branch_length)

tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color("#CC00CC" )

build_tree(tree, 70, 7, 25, 0)

turtle.mainloop()
