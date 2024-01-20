# timer using python

from playsound import playsound
import time
import os

CLEAR = "\033[2J"  # clear terminal screen
CLEAR_AND_RETURN = "\033[H"  # print over the previous output


def alarm(sec):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < sec:
        time.sleep(1)  # wait for a sec
        time_elapsed += 1
        time_left = sec - time_elapsed
        min_left = time_left // 60
        sec_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Alaram will sound in: {min_left:02d}:{sec_left:02d}")
    playsound("alarm.mp3")


min = int(input("how many minutes to wait: "))
sec = int(input("how many seconds to wait: "))
total_sec = min * 60 + sec
alarm(total_sec)
