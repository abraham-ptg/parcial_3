from core import running_msedge
from watch_screen import move_cursor
import time
from get_input import main_input

def main():
    data = main_input()
    running_msedge()
    time.sleep(2)
    move_cursor(data)



if __name__ == "__main__":
    main()