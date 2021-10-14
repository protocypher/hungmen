
from cmd import Cmd
from .game import Game
from .game_exceptions import DuplicateException, GameStateException
from .game_state import GameState
from .game_view import GameView


# ==============================================================================
class GameController(Cmd):
    """
    This controller uses the Cmd class to operate a command shell which drives
    hangman games.

    @author: U{Benjamin Gates<benjamin.j.gates@icloud.com>}
    """

    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Initializes a new controller.
        """

        super().__init__()

        self.view = GameView()
        self.game = None
        self.short = False

        self.prompt = self.view.PROMPT
        self.intro = self.view.INTRO
        self.doc_header = self.view.DOC_HEADER
        self.ruler = self.view.RULER

    # --------------------------------------------------------------------------
    def default(self, arg):
        """
        Handles any unknown commands. If 'short' is on and arg is a single
        letter then that will be considered a guess.

        @param arg: The unknown command line
        @type arg: str
        """

        if not self.short:
            super().default(arg)
        else:
            self.do_guess(arg)

    # --------------------------------------------------------------------------
    def emptyline(self):
        """
        When the player simply presses enter without typing then we will show
        the game update to them.
        """

        self.view.show_update(self.game.hint, self.game.score)

    # --------------------------------------------------------------------------
    def help_new(self):
        """
        Print a command summary when the player asks for help with "new".
        """

        self.view.show_command_help(
            "NEW",
            "new",
            "Initializes and starts a new game."
        )
    
    # --------------------------------------------------------------------------
    def do_new(self, arg):
        """
        Create and begin tracking a new game model.

        @param arg: The command line argument from Cmd
        @type arg: str
        """

        self.view.info("Beginning a new game!")
        self.game = Game()
        self.view.show_update(self.game.hint, self.game.score)

    # --------------------------------------------------------------------------
    def help_guess(self):
        """
        Print a command summary when the player asks for help with "guess".
        """

        self.view.show_command_help(
            "GUESS",
            "guess <letter>",
            "Guesses a letter."
        )

    # --------------------------------------------------------------------------
    def do_guess(self, letter):
        """
        Attempts to guess a letter from the value entered by the user. If it is
        not a valid letter then display an error message and abort. When the
        player guesses a letter that triggers an end condition the player is
        alerted and the model is reset.

        @param letter: The letter to guess
        @type letter: str
        """

        if not self.game:
            self.view.error("Please start a new game before guessing a letter!")
            return
        elif not letter:
            self.view.error("You cannot guess 'nothing'.")
            return
        elif len(letter) > 1:
            self.view.error("You cannot guess more than one letter.")
            return
        elif not letter.isalpha():
            self.view.error("You can only guess letters.")
            return

        try:
            self.game.guess(letter)
        except DuplicateException:
            self.view.error("You already guessed that letter!")
        except GameStateException:
            self.view.system_error("Unexpectd game state; quitting!")
            return True

        if self.game.state is GameState.VICTORY:
            self.view.success("Congradulations! You won!")
            self.view.info(f"The word was {self.game.word}")
            self.game = None
            return

        if self.game.state is GameState.FAILURE:
            self.view.error("I'm sorry, you lost...")
            self.view.info(f"The word was {self.game.word}\n")
            self.game = None
            return

        self.view.show_update(self.game.hint, self.game.score)

    # --------------------------------------------------------------------------
    def help_short(self):
        """
        Print a command summary when the player asks for help with "short".
        """

        self.view.show_command_help(
            "SHORT",
            "short",
            "Toggles whether to allow short guesses."
        )
    
    # --------------------------------------------------------------------------
    def do_short(self, arg):
        """
        Toggles whether the game accepts shortcut guesses.

        @param arg: The command line argument from Cmd
        @type arg: str
        """

        self.short = not self.short
        self.view.info(f"Accepting short guesses: {self.short}")

    # --------------------------------------------------------------------------
    def help_quit(self):
        """
        Print a command summary when the player asks for help with "quit".
        """

        self.view.show_command_help(
            "QUIT",
            "quit",
            "Quits the application."
        )

    # --------------------------------------------------------------------------
    def do_quit(self, arg):
        """
        Prints a fairwell message and quits the game.

        @param arg: The command line argument from Cmd
        @type arg: str
        """

        self.view.info("Good bye; thanks for playing.")
        return True