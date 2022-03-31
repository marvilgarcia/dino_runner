from game.script.actions import Action
from game.shared.point import Point
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from constants import *

import random



class TimedAddObjects(Action):
    """ A timer to determine when the ojects appear on screen

    Responsible is to add a new artifact/object onto the screen

    Attributes: 
        _delay: the amount of time until the next object appears
        _playing_status: True if the player is alive.
    """

    def __init__(self):
        super().__init__()
        self._delay = random.randint(0,3)
        self._counter = 0


    
    def execute(self, cast):
        '''
        Adds an object every three seconds

        Args:
            cast: an instance of cast
        '''

        if self._counter >= (FRAME_RATE * self._delay):
            self._counter = 0
            self._delay = random.randint(0,3)

            text = 'O'

            x = MAX_X - CELL_SIZE
            y =  MAX_Y - CELL_SIZE # will make the gems and rocks start from the bottom.
            position = Point(x, y)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # creating the velocity
            x_v = -int(CELL_SIZE/2)
            y_v = 0
            velocity = Point(x_v, y_v)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_velocity(velocity)
            cast.add_actor("artifacts", artifact)
        else: 
            self._counter += 1
        

        



