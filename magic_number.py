#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# RNG number guessing game

import random


def main():
    # This function sees if the user inputed the magic number

    print("Guess the magic number (0-9)!")

    # Input
    magic_number = int(input("Please enter your guess: "))

    # Process
    random_number = random.randint(0, 9)

    if magic_number == random_number:
        # Output
        print("Nice! Your answer is right!")

    else:
        # Output
        print("Oops! Your answer is wrong!")
        print("The correct answer was: {}".format(random_number))


if __name__ == "__main__":
    main()
