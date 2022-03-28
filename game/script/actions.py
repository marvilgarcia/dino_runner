class Action:
    """
    A thing that is done in the game.

    The responsibility is to execute an action in the game.
    """


    def execute(self, cast, script):
        """
        
        Args:
            cast - an instance of cast containing the actors of the game.
            script - an instance of script containing the actions in the game.
        """

        raise NotImplementedError('Execution is not implemented here.')

