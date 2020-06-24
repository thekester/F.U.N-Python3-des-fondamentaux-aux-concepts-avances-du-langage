#We need the turtle module
import turtle


#avoid calling range for each square
sides = ['east', 'north', 'west' , 'south']

def square(the_turtle, length):
    "have the turtle draw a square of side <length>"
    for side in sides:
        the_turtle.forward(length)
        the_turtle.left(90)
        print(side)
        
#initialize
window = turtle.Screen()
window.title("Caroline et Chloe")

#create first turtle

caroline=turtle.Turtle()
caroline.reset()
caroline.color("hotpink")

chloe=turtle.Turtle()
chloe.reset()
chloe.color("lightgreen")
        
#alternate : turtle , twist and square size
contexts = ((caroline ,  15 , 100 , ),
            (chloe , 60 , 30 ),
           )
#initialize alternating contexts
cycle = len(contexts)
counter = -1

#the callback triggered when an user clicks in x,y
def clicked(x,y):
    global counter
    counter += 1
    #alternate between the various contexts
    (turtle, twist , size) = contexts[counter % cycle ]
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(twist)
    square(turtle,size)

# arm callback
window.onscreenclick(clicked)
#turtle.onscreenclick(clicked)

#user can quit by typing 'q'
window.onkey(window.bye , 'q')
window.listen()


# read & dispatch events
turtle.mainloop()



