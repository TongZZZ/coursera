# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:15:08 2013

"""

import random
def name_to_number(name):
    if name  == 'rock': 
        return 0
    elif name  == 'Spock': 
        return 1
    elif name == 'paper': 
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else: 
        print 'Name not recognizable! Try again!'

def number_to_name(num):
    if num == 0:
        return 'rock'
    elif num == 1:
        return 'Spock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'lizard'
    elif num == 4:
        return 'scissors'
    else:
        print 'Number not recognizable! Something is Wrong!'

def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5,1)
    if (player_number - comp_number) % 5 in (1,2):
        print ""
        print "Player chooses %s\nComputer chooses %s\nPlayer wins!" %(number_to_name(player_number),number_to_name(comp_number))
    elif (player_number - comp_number) % 5 in (3,4):
        print ""
        print "Player chooses %s\nComputer chooses %s\nComputer wins!" %(number_to_name(player_number),number_to_name(comp_number))
    elif (player_number - comp_number) % 5 == 0:
        print ""
        print "Player chooses %s\nComputer chooses %s\nPlayer and computer tie!" %(number_to_name(player_number),number_to_name(comp_number))

#rpsls('rock')
#rpsls('rock')
#rpsls('scissors')
