from .scaffold import SCAFFOLD
from colorama import init, Fore, Style
from textwrap import dedent

init(autoreset=True)

# ==============================================================================
COLOR_CODES = {
    "@!": Style.RESET_ALL,
    "@w": Fore.WHITE + Style.DIM,
    "@W": Fore.WHITE + Style.BRIGHT,
    "@k": Fore.BLACK + Style.DIM,
    "@K": Fore.BLACK + Style.BRIGHT,
    "@b": Fore.BLUE + Style.DIM,
    "@B": Fore.BLUE + Style.BRIGHT,
    "@c": Fore.CYAN + Style.DIM,
    "@C": Fore.CYAN + Style.BRIGHT,
    "@g": Fore.GREEN + Style.DIM,
    "@G": Fore.GREEN + Style.BRIGHT,
    "@y": Fore.YELLOW + Style.DIM,
    "@Y": Fore.YELLOW + Style.BRIGHT,
    "@r": Fore.RED + Style.DIM,
    "@R": Fore.RED + Style.BRIGHT,
    "@m": Fore.MAGENTA + Style.DIM,
    "@M": Fore.MAGENTA + Style.BRIGHT
}


# ==============================================================================
class GameView:
    """
    Provides color coded output actions and established UI element values.

    @author: U{Benjamin Gates<benjamin.j.gates@icloud.com>}
    """

    _PROMPT = "\n@B>@! "
    _INTRO = "\n@CWelcome to HungMen!@c ('?' for help)@!"
    _DOC_HEADER = "\n@CCommands@c (? <command>)@!"
    _RULER = "@B-@!"

    # --------------------------------------------------------------------------
    @staticmethod
    def parse(message):
        """
        Given a string, replace all @ codes with appropriate color codes.

        @param message: The string to parse
        @type message: str

        @return: A parsed string
        @rtype: str
        """

        for code, ansi in COLOR_CODES.items():
            message = message.replace(code, ansi)
        
        return message

    # --------------------------------------------------------------------------
    @property
    def PROMPT(self):
        """
        The color coded command prompt.

        @type: str
        """

        return self.parse(GameView._PROMPT)

    # --------------------------------------------------------------------------
    @property
    def INTRO(self):
        """
        The color coded introduction banner.

        @type: str
        """

        return self.parse(GameView._INTRO)
    
    # --------------------------------------------------------------------------
    @property
    def DOC_HEADER(self):
        """
        The color coded help banner.

        @type: str
        """

        return self.parse(GameView._DOC_HEADER)

    # --------------------------------------------------------------------------
    @property
    def RULER(self):
        """
        The color coded ruler character.

        @type: str
        """

        return self.parse(GameView._RULER)

    # --------------------------------------------------------------------------
    def success(self, message):
        """
        Prints a message in a success style.

        @param message: The message to print
        @type message: str
        """

        print(self.parse(f"\n@G{message}"))

    # --------------------------------------------------------------------------
    def info(self, message):
        """
        Prints a message in an informative style.

        @param message: The message to print
        @type message: str
        """

        print(self.parse(f"\n@W{message}"))

    # --------------------------------------------------------------------------
    def warn(self, message):
        """
        Prints a message in a warning style.

        @param message: The message to print
        @type message: str
        """

        print(self.parse(f"\n@Y{message}"))
    
    # --------------------------------------------------------------------------
    def error(self, message):
        """
        Prints a message in an error style.

        @param message: The message to print
        @type message: str
        """

        print(self.parse(f"\n@R{message}"))
    
    # --------------------------------------------------------------------------
    def system_error(self, message):
        """
        Prints a message in a system error style.

        @param message: The message to print
        @type message: str
        """

        print(self.parse(f"\n@M{message}"))

    # --------------------------------------------------------------------------
    def show_command_help(self, label, example, description):
        """
        Prints help for a command based on the given elements.

        @param label: The header label
        @type label: str
        @param example: An example of the command's usage
        @type example: str
        @param description: A brief description of the command's purpose
        @type description: str
        """

        print(self.parse(f"\n@Y--=< @C{label} @Y>=--"))
        print(self.parse(f"@G{example}"))
        print(self.parse(f"{description}"))

    # --------------------------------------------------------------------------
    def show_update(self, hint, score):
        """
        Shows the current status of the game to the player by showing them the
        hangman graphic appropriate for their score and a hint appropriate for
        the guesses they've made.

        @param hint: The hint to display
        @type hint: str
        @param score: The score to lookup the hangman graphic with
        @type score: int
        """

        scaffold = dedent(SCAFFOLD[score])
        print(self.parse(f"@w{scaffold}"))
        print(self.parse(f"@C{hint}"))
