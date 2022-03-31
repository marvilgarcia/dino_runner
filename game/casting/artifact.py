from game.casting.actor import Actor


class Artifact(Actor):
    """
    An object that moves across the screen.

    
    """
    def __init__(self):
        super().__init__()
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message