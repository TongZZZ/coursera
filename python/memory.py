#http://www.codeskulptor.org/#user24_VqG7ZHjKWP_52.py
# implementation of card game - Memory

import simplegui
import random
import math
global numbers,numbers_copy1,numbers_copy2,numbers_ready,exposed,turns
turns = 0
# helper function to initialize globals
def new_game():
    global numbers,numbers_copy1,numbers_copy2,numbers_ready,exposed, state, turns
    state = 0
    numbers1=range(8)
    numbers2=range(8)
    random.shuffle(numbers1)
    numbers_copy1 = numbers1
    random.shuffle(numbers2)
    numbers_copy2 = numbers2
    numbers_ready = numbers_copy1 + numbers_copy2
    exposed = ["False"]*16
    turns = 0 
    label.set_text("Turns = "+str(turns))

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,state,card_click1,card_click2
    global turns

    if state == 0:
        card_click1 = math.floor(pos[0]/50)
        if exposed[card_click1] == 'True':
            state = 0
        else: 
            exposed[card_click1] = 'True'
            state = 1
    elif state == 1:
        card_click2 = math.floor(pos[0]/50)
        if exposed[card_click2] == 'True':
            state = 1
        else:
            exposed[card_click2] = 'True'
            state = 2

    else:
        turns = turns+1
        label.set_text("Turns = "+str(turns))
        if numbers_ready[card_click1] != numbers_ready[card_click2]:
            exposed[card_click1] = 'False'
            exposed[card_click2] = 'False'
        card_click1 = math.floor(pos[0]/50)
        if exposed[card_click1] == 'True':
            state = 0
        else: 
            exposed[card_click1] = 'True'
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in xrange(16):
        canvas.draw_text(str(numbers_ready[i]), (20+i*50, 60), 30, 'White')
    for i in xrange(16):
        if exposed[i] == 'False':
            canvas.draw_polygon([(0+50*i, 0), (50+50*i, 0),(50+50*i,100),(0+50*i,100)], 1, 'White','Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
