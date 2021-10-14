from enum import Enum


# ==============================================================================
class GameState(Enum):
    """
    The state of the game model is trinary: Playing, Failure and Victory.
    """

    PLAYING = 1
    FAILURE = 2
    VICTORY = 3