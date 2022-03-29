from isodate import Duration
from game.script.actions import Action
from game.shared.point import Point
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from constants import *

import time 
import datetime 
import random



class TimedAddObjects(Action):
    """ A timer to determine when the ojects appear on screen

    Responsible is to add a new artifact/object onto the screen

    Attributes: 
        _delay: the amount of time until the next object appears
        _playing_status: True if the player is alive.
    """

    def __init__(self, delay, playing_status):
        self._delay = delay
        self._playing_status = playing_status
        self._counter = 0


    def get_delay(self):

        return self._delay


    def set_delay(self, delay):
        
        self._delay = delay 

    
    def execute(self, cast, script):
        '''
        Adds an object every two seconds
        '''
        # add a object after every two seconds.

        self._counter += 1
        # idea from Brother Hunter
        if self._counter == (FRAME_RATE * self._delay):
            self._counter = 0
            text = 'O'

            x = ROWS - 1
            y = 599  # will make the gems and rocks start from the bottom.
            position = Point(x, y)
            # scales the pixel to the appropriate size.
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # creating the velocity
            x_v = -2
            y_v = 0
            velocity = Point(x_v, y_v)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            # changes the velocity
            artifact._velocity = velocity  # changes to 0,2
            # makes the velocity work or switches it on. Move next from actor class
            artifact.move_next(MAX_X, MAX_Y)
            cast.add_actor("artifacts", artifact)

        # my idea
        # duration = self._delay
        # while self._playing_status == True:
        #     # how to loop back through and make it set a new timer
        #         # set a variable equal to 1 when duration = 0 change to value 
        #     while duration > 0:
        #         # represents a duration
        #         datetime.timedelta(seconds=duration)

        #         # Suspend execution of the calling thread for the given number of seconds.
        #         time.sleep(1)

        #         duration -= 1
            
        #     text = "o"

        #     x = ROWS - 1
        #     y = 599  # will make the gems and rocks start from the bottom.
        #     position = Point(x, y)
        #     # scales the pixel to the appropriate size.
        #     position = position.scale(CELL_SIZE)

        #     r = random.randint(0, 255)
        #     g = random.randint(0, 255)
        #     b = random.randint(0, 255)
        #     color = Color(r, g, b)

        #     # creating the velocity
        #     x_v = -2
        #     y_v = 0
        #     velocity = Point(x_v, y_v)

        #     artifact = Artifact()
        #     artifact.set_text(text)
        #     artifact.set_font_size(FONT_SIZE)
        #     artifact.set_color(color)
        #     artifact.set_position(position)
        #     # changes the velocity
        #     artifact._velocity = velocity  # changes to 0,2
        #     # makes the velocity work or switches it on. Move next from actor class
        #     artifact.move_next(MAX_X, MAX_Y)
        #     cast.add_actor("artifacts", artifact)



