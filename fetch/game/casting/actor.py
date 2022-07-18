from game.casting.text import Text


class Actor:
    """A thing that participates in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new Actor using the given group and id.
        
        Args:
            group: A string containing the actor's group name.
            id: A number that uniquely identifies the actor within the group.
        """
        self._debug = debug
        self._points = 0 
        
    def is_debug(self):
        """Whether or not the actor is being debugged.
        
        Returns:
            True if the actor is being debugged; False if otherwise.
        """
        return self._debug
    
    def get_points(self):
        """ Get points.
        
        Returns:
            points.
        """
        return self._points
        
    def set_points(self, points):
        """ Set points.
        
        Args:
            points
        """
        self._points = points