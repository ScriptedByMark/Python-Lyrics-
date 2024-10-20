import sys
import time

def print_lyrics():
    lines = [
        ("Secrets I have held in my heart,", 0),
        ("Are harder to hide than I thought,", 0),
        ("Maybe I just wanna be yours,", 0.09),
        ("I wanna be yours,", 0.09),
        ("I wanna be yours,", 0.15),
        ("Wanna be yours,", 0.17),
        ("Wanna be yours,", 0.22),
        ("Wanna be yours,", 0.19)
    ]

    for line, char_delay in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()

print_lyrics()
