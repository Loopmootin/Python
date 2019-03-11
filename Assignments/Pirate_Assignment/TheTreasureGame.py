# Imports

import random
from Pirates import Pirate


# Objects

username = input("Enter your most terrifying pirate name : ")
usernumber = input("Enter your lucky Treasure Game number : ")

gamenumber = int(usernumber)

P1 = Pirate(username)
P2 = Pirate("Kenny Klap For Øjet")
P3 = Pirate("Torsten Træben")
P4 = Pirate("Per Pirathat")


# Lists

listOfPirates = [P1, P2, P3, P4]
listLength = len(listOfPirates)


# Functions

def resetPointers():
    i = 0

    for p in listOfPirates:
        if i < listLength - 1:
            listOfPirates[i].setPointer(listOfPirates[i+1]._name)
            i = i + 1
        elif i == listLength - 1:
            listOfPirates[i].setPointer(listOfPirates[0]._name)
            if listOfPirates[i]._name == listOfPirates[0]._name:
                if listOfPirates[i]._name == username:
                    print("You're the last one left, congratulations", listOfPirates[i]._name)
                    exit()
                else:
                    print("Awww you didn't win, but better luck next time! The winner is", listOfPirates[i]._name)
                    exit()
        else:
            print("Can i get some rum?")


def showPointers():
    x = 0

    for p in listOfPirates:
        if x <= listLength:
            print("This pirate is called", listOfPirates[x].getName(), "and he points to pirate", listOfPirates[x].getPointer())
            x = x + 1
        else:
            print("Can i get some kebab?")


# Setting up Pirates

resetPointers()

print("There are", len(listOfPirates), "pirates in the Treasure Game")
print()

showPointers()
print()


# Setting up Treasure Game

while listLength > 1:
    treasureGameNumber = gamenumber
    i = 0

    print()
    print("The Treasure Game Number chooses: ")
    while i < treasureGameNumber:
        pirateJump = random.choice(listOfPirates)
        print(pirateJump._name)
        i = i + 1
        index = listOfPirates.index(pirateJump)

    print()
    print("And the pirate that has to jump is number", index, "who is", listOfPirates[index]._name)
    print()
    listOfPirates.pop(index)

    listLength = len(listOfPirates)
    print("There are", len(listOfPirates), "pirates left in the Treasure Game")
    print()

    resetPointers()

    showPointers()
