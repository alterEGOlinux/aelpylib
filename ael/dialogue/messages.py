## ----------------------------------------------------------------------------
##             { alterEGO Linux: "Open the vault of knowledge" }             ##
## ----------------------------------------------------------------------------
##
## /ael/dialogue/messages.py
##   created        : 2022-11-21 12:02:56 UTC
##   updated        : 2022-11-21 12:02:56 UTC
##   description    : Messages
## ____________________________________________________________________________

from ael.dialogue.colors import Colors

def message(category, msg):

    if category == 'action':
        print(f"{Colors.GREEN}[*]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'result':
        print(f"{Colors.BLUE}[-]{Colors.RESET} {msg}")
    elif category == 'question':
        ## The input will be in variable `answer`.
        answer = input(f"{Colors.BLUE}[?]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'alert':
        print(f"{Colors.YELLOW}[!]{Colors.RESET} {msg}")
    elif category == 'warning' or category == 'error':
        print(f"{Colors.RED}[!]{Colors.RESET} {Colors.BOLD}{msg}{Colors.RESET}")
    elif category == 'title':
        print(f"{Colors.BOLD}{msg}{Colors.RESET}")


# vim: foldmethod=marker
## ___________________________{ FIN ¯\_(ツ)_/¯ }_______________________________
