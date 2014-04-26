#http://www.codeskulptor.org/#user23_V0QqB4nk27_163.py
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-random.randrange(120, 240)/60,  random.randrange(60, 180) / 60.0]
paddle1_pos = 0
paddle2_pos = 0
score1 = 0
score2 = 0 
paddle1_vel = 0
paddle2_vel = 0    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global paddle1_pos, paddle2_pos
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction =='right':
        ball_vel = [random.randrange(120, 240)/60,  random.randrange(60, 180)/60.0]
    if direction == 'left':
        ball_vel = [-random.randrange(120, 240)/60,  random.randrange(60, 180)/60.0]
    paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT -1
    paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT -1

# define event handlers
def new_game():
    global ball_pos, ball_vel
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    foo = ['left', 'right']
    random_index = random.randrange(0,len(foo))
    spawn_ball(foo[random_index])
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel

        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        if abs(ball_pos[1] - (paddle1_pos+HALF_PAD_HEIGHT))<=HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else: 
            spawn_ball('right')
            score2 = score2 + 1
    if (ball_pos[0]>= WIDTH - PAD_WIDTH - BALL_RADIUS-1):
        if abs(ball_pos[1] - (paddle2_pos+HALF_PAD_HEIGHT))<=HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else: 
            spawn_ball('left')
            score1 = score1 + 1
        
    if (ball_pos[1] <= BALL_RADIUS or ball_pos[1]>= HEIGHT - BALL_RADIUS-1):
        ball_vel[1] = - ball_vel[1]
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos <= 0:
        paddle1_pos = 0
    elif paddle1_pos >=  HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    else: pass
    
    if paddle2_pos <= 0:
        paddle2_pos = 0
    elif paddle2_pos >=  HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    else: pass
    
    # draw paddles
    c.draw_polygon([(0, paddle1_pos), (0, PAD_HEIGHT+paddle1_pos),(PAD_WIDTH,PAD_HEIGHT+paddle1_pos), (PAD_WIDTH, paddle1_pos)], 1, 'Blue','Blue')
    c.draw_polygon([(WIDTH, paddle2_pos), (WIDTH, PAD_HEIGHT+paddle2_pos),(WIDTH-PAD_WIDTH,PAD_HEIGHT+paddle2_pos), (WIDTH-PAD_WIDTH, paddle2_pos)], 1, 'Blue','Blue')
    # draw scores
    c.draw_text(str(score1) + " | " + str(score2), (420, 50), 36, 'Blue')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc    
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc 
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0    
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game,100)


# start frame
new_game()
frame.start()
