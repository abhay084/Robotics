# welcome to the main menu
from project_test import *
from Subway import *
from diagno import *

while True:
    print("\nMain Menu\n")
    t = (input("Enter (1) to play \"Rock Paper Scissor\" \nEnter (2) to play \"Dinosour\" \nOr Enter anything else to exit\n"))

    if t == "1":
        print("\nPlaying \"Rock Paper Scissor\"...")
        rps()


    elif t == "2":
        print("\nPlaying \"Dinosour\"...")
        dino()


    else:
        print("\nExiting...")
        break