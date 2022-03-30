from tkinter.tix import MAX

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

    def __init__(self, delay):
        super().__init__()
        self._delay = delay
        self._counter = 0


    
    def execute(self, cast, script):
        '''
        Adds an object every three seconds
        '''

        # idea from Brother Hunter
        if self._counter >= (FRAME_RATE * self._delay):
            self._counter = 0

            text = 'O'

            x = MAX_X - 1
            y =  MAX_Y - 1 # will make the gems and rocks start from the bottom.
            position = Point(x, y)
            # scales the pixel to the appropriate size.
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # creating the velocity
            x_v = -3
            y_v = 0
            velocity = Point(x_v, y_v)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            # changes the velocity
            artifact._velocity = velocity  
            # makes the velocity work or switches it on. Move next from actor class
            artifact.move_next(MAX_X, MAX_Y)
            cast = Cast()
            cast.add_actor("artifacts", artifact)
        else: 
            self._counter += 1

        



