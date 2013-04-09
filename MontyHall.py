#!/usr/bin/env python
# Written by: DGC

# python imports
import random
# local imports

def auto_monty_hall():
    # set up 3 doors, one of which is a car the other two are goats
    doors = []
    for i in range(3):
        doors.append("goat")
    car_number = random.randrange(3)
    doors[car_number] = "car"

    # the computer guesses a door
    guess = random.randrange(3)

    # now find a goat that the computer hasn't guessed and 'reveal it' so that 
    # the computer doesn't gues it
    num = -1
    result = "car"
    while(result == "car"):
        num = random.randrange(3)
        if (num == guess):
            continue
        result = doors[num]
    # always switch to the other door which has not been shown
    for i in range(3):
        if (i == num):
            continue
        if (i == guess):
            continue
        if (doors[i] == "goat"):
            return False
        else:
            return True

if (__name__ == "__main__"):
    count = 0
    limit = 1000000
    for i in range(limit):
        if(auto_monty_hall()):
            count += 1
    print(str(count) + " cars in " + str(limit) + " tries.")
