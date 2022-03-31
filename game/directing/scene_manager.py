# import all required classes
from constants import * 

# Casting
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

# script 
from script.actions import Action
from script.script import Script
from script.timed_add_objects import TimedAddObjects

# services
from services.keyboard_service import KeyboardService
from services.video_service import VideoService

class SceneManager: # look up scene_manager from batter-complete

    # create an instance of every class
    TIMEDADDOBJECTS = TimedAddObjects(cast, script)

    def __init__(self):
        
        pass

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    def _prepare_new_game(self):
        pass

    def _prepare_try_again(self):
        pass
    
    def _prepare_game_over(self):
        pass


    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------

    # create functions for the casting objects 

    def _add_objects(self, script):
        script.clear_actions(UPDATE)
        script.add_actions(UPDATE, TimedAddObjects(DELAY))
