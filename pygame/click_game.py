ball = Actor('character_n')
ball.pos = 100, 50

WIDTH =500
HEIGHT = 300

def draw():
    screen.fill((51,17,34))
    ball.draw()

def update():
    ball.left = ball.left + 501
    if ball.left > WIDTH:
        ball.right = 0

