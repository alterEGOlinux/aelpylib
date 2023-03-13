# -----------------------------------------------------------------------------
#              { alterEGO Linux: "Open the vault of knowledge" }
# -----------------------------------------------------------------------------
#
# /ael/timing.py
#   created        : 2023-03-13 00:08:39 UTC
#   updated        : 2023-03-13 11:36:22 UTC
#   description    : Time related stuff
# _____________________________________________________________________________

from functools import wraps
import time

def time_of_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print(f'[*] {func.__name__} executed in {round(finish-start, 2)} seconds(s)')
    return wrapper

if __name__ == '__main__':
    pass

# -----------------------------------------------------------------------------
# vim: foldmethod=marker
# ____________________________{ FIN ¯\_(ツ)_/¯ }_______________________________
