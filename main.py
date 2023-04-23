import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')
score = 0
gamer_over = False

#turtle list
turtle_list = []


#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdow_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85

    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size = 10
def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

        #print(x, y)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2)
    t.color("green")
    t.goto(x * grid_size , y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive_function
def show_turtles_randomly():
    if not gamer_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 1000)

def countdown(time):
    global gamer_over
    countdow_turtle.hideturtle()
    countdow_turtle.color("dark green")
    countdow_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    countdow_turtle.setpos(0, y - 40)
    countdow_turtle.clear()

    if time > 0:
        countdow_turtle.clear()
        countdow_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time -1),1000)
    else:
        gamer_over = True
        countdow_turtle.clear()
        hide_turtles()
        countdow_turtle.write(arg="Game Over", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    hide_turtles()
    turtle.tracer(1)

start_game_up()
turtle.mainloop()