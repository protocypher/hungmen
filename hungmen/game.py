from random import choice
from .game_state import GameState
from .game_exceptions import DuplicateException, GameStateException


# ==============================================================================
class Game:
    """
    This model tracks the progress of a single, hangman game.

    @author: U{Benjamin Gates<mailto:benjamin.j.gates@icloud.com>}
    """

    MAX_SCORE = 6

    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Initializes a new game of hangman.
        """

        with open("words.txt", mode="r") as w:
            words = w.readlines()
            self._word = choice(words).strip()

        self._letters = set(self.word)
        self._guesses = set()
        self._state = GameState.PLAYING

    # --------------------------------------------------------------------------
    @property
    def word(self):
        """
        The target word to guess for this game.

        @type: str
        """

        return self._word
    
    # --------------------------------------------------------------------------
    @property
    def letters(self):
        """
        A unique set of letters that C{word} contains.
    
        @type: set
        """

        return self._letters
    
    # --------------------------------------------------------------------------
    @property
    def guesses(self):
        """
        A unique set of the letters which have been guessed by the player.

        @type: set
        """

        return self._guesses

    # --------------------------------------------------------------------------
    @property
    def hint(self):
        """
        A masked version of the game word that only shows the letters which have
        been correctly guessed.
    
        @type: str
        """

        h = []

        for letter in self.word:
            h.append(letter if letter in self._guesses else "_")
        
        return " ".join(h)
    
    # --------------------------------------------------------------------------
    @property
    def tally(self):
        """
        The total number of valid guesses made by the player. Duplicate guesses
        do not count against the player's score.

        @type: int
        """

        return len(self._guesses)
    
    # --------------------------------------------------------------------------
    @property
    def score(self):
        """
        The number of valid, wrong guesses made by the player. Duplicate guesses
        do not count against the player's score.

        @type: int
        """

        return len(self._guesses - self.letters)

    # --------------------------------------------------------------------------
    @property
    def state(self):
        """
        The current state of the game.

        @type: GameState
        """

        return self._state

    # --------------------------------------------------------------------------
    def guess(self, letter):
        """
        Guesses the given C{letter} in this game.

        @param letter: The letter being guessed
        @type letter: str

        @returns: The updated GameState
        @rtype: GameState

        @raise DuplicateException: If letter has already been guessed
        @raise GameStateException: If state is not PLAYING
        """

        if self.state is not GameState.PLAYING:
            raise GameStateException(f"Bad state: {self.state}")

        if letter.upper() in self.guesses:
            raise DuplicateException(f"Duplicate letter: {letter}")

        self.guesses.add(letter.upper())

        if self.guesses >= self.letters:
            self._state = GameState.VICTORY
        elif self.score > Game.MAX_SCORE:
            self._state = GameState.FAILURE
        
        return self.state
