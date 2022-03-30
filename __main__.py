import os
import random 
from constants import *
from tkinter.tix import MAX
from game.casting.dino import Dino
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.script.script import Script

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

from constants import *



def main():
    
    # create the cast
    cast = Cast()
    script = Script()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2 )
    y = int(MAX_X / -65)
    position = Point(x, y)

    robot = Dino()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    
    for n in range(DEFAULT_ARTIFACTS):
 
        text = random.choice(["o","o"])
        message = [n] 
        
        x = random.randint(1, ROWS - 1) 
        y = int(540 / CELL_SIZE)  # will make the gems and rocks start from the bottom. 
        position = Point(x, y)
        position = position.scale(CELL_SIZE) # scales the pixel to the appropriate size.

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # creating the velocity
        x_v = random.randrange(1,5)
        y_v = 0
        velocity = Point(x_v, y_v)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # changes the velocity
        artifact._velocity = velocity # changes to 0,2
        artifact.move_next(MAX_X, MAX_Y) #makes the velocity work or switches it on. Move next from actor class
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
