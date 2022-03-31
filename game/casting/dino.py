from game.casting.actor import Actor
from game.shared.point import Point

class Dino(Actor):
    
    def __init__(self):
        super().__init__()
        self._gravity = 25  # int(30 / 2) 5 int(30 / 2) This is how we create gravity Changing to higher numbers makes it fall faster. 
        
    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y() + self._gravity) 
        # checks if y is below floor creates the floor at the bottom making it so the dino does not fall down more. 
       
        if y >= 570:
            y = 570 
            
        #checks to see if y is at the top and stops dino at the top of the screen
        if y <= 475: #30 * 2:
            y =475 #30 * 2
            
        
        self._position = Point(x, y)
        
       
        
       