import turtle as t
import random as rd

t.bgcolor('white')

arrow = t.Turtle()
arrow.shape('arrow')
arrow.color('red')
arrow.speed(0)
arrow.penup()
arrow.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start game',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = arrow.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    arrow.color('red')
    leaf.color('red')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    arrow_speed = 2
    arrow_length = 3
    arrow.shapesize(1,arrow_length,1)
    arrow.showturtle()
    display_score(score)
    place_leaf()

    while True:
        arrow.forward(arrow_speed)
        if arrow.distance(leaf)<20:
            place_leaf()
            arrow_length = arrow_length + 1
            arrow.shapesize(1,arrow_length,1)
            arrow_speed = arrow_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if arrow.heading() == 0 or arrow.heading() == 180:
        arrow.setheading(90)

def move_left():
    if arrow.heading() == 90 or arrow.heading() == 270:
        arrow.setheading(180)

def move_down():
    if arrow.heading() == 0 or arrow.heading() == 180:
        arrow.setheading(270)

def move_right():
    if arrow.heading() == 90 or arrow.heading() == 270:
        arrow.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
