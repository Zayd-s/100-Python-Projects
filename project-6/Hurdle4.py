def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():    
        jump()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
