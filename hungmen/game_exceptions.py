# ==============================================================================
class DuplicateException(Exception):
    """
    Raised when duplicate values are encountered.
    """

    def __init__(self, message):
        super().__init__(message)


# ==============================================================================
class GameStateException(Exception):
    """
    Raised when an operation is attempted in the wrong GameState.
    """

    def __init__(self, message):
        super().__init__(message)
