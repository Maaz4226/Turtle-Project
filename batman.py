import turtle  

def draw_batman_logo():
    bat = turtle.Turtle()
    bat.turtlesize(1, 1, 1)
    bat.pensize(2)
    bat.color("yellow", "black")
    bat.speed(3)

    bat.begin_fill()

    bat.left(90)
    bat.circle(50, 85)
    bat.circle(15, 110)
    bat.right(180)
    bat.circle(30, 150)
    bat.right(5)
    bat.forward(10)
    bat.right(90)
    bat.circle(-70, 140)
    bat.forward(40)
    bat.right(110)
    bat.circle(100, 30)
    bat.circle(30, 100)
    bat.left(50)
    bat.forward(50)
    bat.right(145)
    bat.forward(30)
    bat.left(55)
    bat.forward(10)

    bat.forward(10)
    bat.left(55)
    bat.forward(30)
    bat.right(145)
    bat.forward(50)
    bat.left(50)
    bat.circle(30, 100)
    bat.circle(100, 30)
    bat.right(90)
    bat.right(20)
    bat.forward(40)
    bat.circle(-70, 140)
    bat.right(90)
    bat.forward(10)
    bat.right(5)
    bat.circle(30, 150)
    bat.left(180)
    bat.circle(15, 110)
    bat.circle(50, 85)

    bat.end_fill()

    bat.penup()
    bat.goto(-0, 55)
    bat.pendown()

    bat.color('yellow')
    bat.write("BATMAN", align='center', 
              font=("Shrikhand", 20, "bold"))
    
    bat.hideturtle()

def setup_screen():
    wn = turtle.Screen()
    wn .bgcolor("black")
    wn.title("Batman")

if __name__ == "__main__":
    setup_screen()
    draw_batman_logo()
    turtle.done()