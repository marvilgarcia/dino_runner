from turtle import Turtle
from game.casting.actor import Actor
from game.shared.point import Point
from game.script.timed_add_objects import TimedAddObjects
import time
from constants import * 

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._total_score = 0 
        self._is_game_over = False
        self._counter = 0
        
    def start_game(self, cast, script):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast, script)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast, script):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        self._game_score()

        add_object = TimedAddObjects(DELAY)
        add_object.execute(cast, script)
        # think I will need to return the artifacts as a list so the loop can happen below.
        # but once an actor is added in the timed_add_objects class then it will be put in the list above
        # if timed_add_objects inherits from action do I need to have that somewhere in this? no
        # it would
        
        banner.set_text(str(f'Score: {self._total_score}')) 
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # becuase it is a list it has to loop through.
        for artifact in artifacts:
            artifact.move_next(max_x, max_y) # this updates it on the game so it goes from top to bottom.
            if robot.get_position().equals(artifact.get_position()):
                text = artifact.get_text() 
                if text == "o":
                    self._is_game_over = True
                    x = int(450)
                    y = int(300)
                    position = Point(x, y)
                    # write game over 
                    message = Actor()
                    message.set_text("Game over")
                    message.set_position(position)
                    cast.add_actor("messages", message)
            
                
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        
        
    def _game_score(self):
        '''
        Adds a point every second the game is played.
        '''
        if self._is_game_over:
            return 
        if self._counter >= (12):
            self._counter = 0
            self._total_score += 1
        else:
            self._counter += 1
        
