import time

ball = Actor('character_n')
ball.pos = 100, 50

WIDTH =500
HEIGHT = 300

def draw():
    screen.fill((51,17,34))
    ball.draw()

def set_ball_sad():
    ball.image:'character_H'

def update():
    ball.left = ball.left + 6
    if ball.left > WIDTH:
        ball.right = 0

def on_mouse_down(pos):
    if ball.collidepoint(pos):
        sounds.grunt.play()
        set_ball_sad()
        ball.image='character_h'
        time.sleep(1)

        print("You monster!")
    else:
        sounds.boing.play()
        print("BUt luCk NExT tIMe STo0biD!")

