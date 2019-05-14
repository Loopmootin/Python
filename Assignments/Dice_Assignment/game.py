# imports
import random
from dice import Die

# creating the dice from Die class
red_die = Die("Red", [0, 0, 4, 4, 8, 8], [])
green_die = Die("Green", [2, 2, 3, 3, 7, 7], [])
blue_die = Die("Blue", [1, 1, 5, 5, 6, 6], [])

# calling the winner
the_winner = "Wait what, no winner??"

# input from user
numberofdice = int(input("Choose number of players(2 or 3): "))
numberofrolls = int(input("Choose number of rolls: "))


# if using 2 colors
def roll_die_2():
    i = 0
    num = numberofrolls
    # setting global to reuse same variable outside function
    global first_player, second_player

    # setting first players color
    if(choose_player1.lower() == "red"):
        first_player = red_die
    elif(choose_player1.lower() == "green"):
        first_player = green_die
    elif(choose_player1.lower() == "blue"):
        first_player = blue_die
    else:
        print("Something went wrong")

    # setting second players color and checking if not the same as first
    if(choose_player2.lower() == "red" and choose_player1.lower() != "red"):
        second_player = red_die
    elif(choose_player2.lower() == "green"
            and choose_player1.lower() != "green"):
        second_player = green_die
    elif(choose_player2.lower() == "blue"
            and choose_player1.lower() != "blue"):
        second_player = blue_die
    else:
        print("You need to choose a different color than player 1!")

    # amount of rolls is decided by user when program is running
    while i < num:
        roll1 = random.choices(first_player.getSides())[0]
        roll2 = random.choices(second_player.getSides())[0]
        if(roll1 > roll2):
            first_player.getScores().append("+")
        else:
            second_player.getScores().append("+")
        i = i + 1


# if using all 3 colors
def roll_die_3():
    i = 0
    num = numberofrolls

    # amount of rolls is decided by user when program is running
    while i < num:
        roll1 = random.choices(red_die.getSides())[0]
        roll2 = random.choices(green_die.getSides())[0]
        roll3 = random.choices(blue_die.getSides())[0]
        if(roll1 > roll2 and roll1 > roll3):
            red_die.getScores().append("+")
        elif(roll2 > roll1 and roll2 > roll3):
            green_die.getScores().append("+")
        elif(roll3 > roll1 and roll3 > 2):
            blue_die.getScores().append("+")
        i = i + 1


# chosing which function to run and what to print from the results
if(numberofdice == 2):
    choose_player1 = input("Choose which color die " +
                           "you want [Red, Green, Blue]: ")
    # calling the Die toString() 
    if(choose_player1.lower() == "red"):
        print(red_die.toString())
    elif(choose_player1.lower() == "green"):
        print(green_die.toString())
    elif(choose_player1.lower() == "blue"):
        print(blue_die.toString())
    else:
        print("You must chose one of the 3 colors!")

    choose_player2 = input("Choose which color die " +
                           "you want [Red, Green, Blue]: ")
    # calling the Die toString()
    if(choose_player2.lower() == "red"):
        print(red_die.toString())
    elif(choose_player2.lower() == "green"):
        print(green_die.toString())
    elif(choose_player2.lower() == "blue"):
        print(blue_die.toString())
    else:
        print("You must chose one of the 3 colors!")

    # calling function
    roll_die_2()

    # checking and calling the winner
    if(len(first_player.getScores()) > len(second_player.getScores())):
        the_winner = first_player.getColor() + " is the winner!"
    else:
        the_winner = second_player.getColor() + " is the winner!"

    print(str(first_player.getColor()) + " : " +
          str(len(first_player.getScores())))
    print(str(second_player.getColor()) + " : " +
          str(len(second_player.getScores())))
    print(the_winner)

elif(numberofdice == 3):
    # calling function
    roll_die_3()

    # checking and calling the winner
    if(len(red_die.getScores()) > len(green_die.getScores()) and
       len(red_die.getScores()) > len(blue_die.getScores())):
        the_winner = red_die.getColor() + " is the winner!"
    elif(len(green_die.getScores()) > len(red_die.getScores()) and
         len(green_die.getScores()) > len(blue_die.getScores())):
        the_winner = green_die.getColor() + " is the winner!"
    elif(len(blue_die.getScores()) > len(red_die.getScores()) and
         len(blue_die.getScores()) > len(green_die.getScores())):
        the_winner = blue_die.getColor() + " is the winner!"
    else:
        the_winner = "Something went very wrong here!"

    print(red_die.toString())
    print(green_die.toString())
    print(blue_die.toString())
    print(str(red_die.getColor()) + " : " + str(len(red_die.getScores())))
    print(str(green_die.getColor()) + " : " + str(len(green_die.getScores())))
    print(str(blue_die.getColor()) + " : " + str(len(blue_die.getScores())))
    print(the_winner)

else:
    print("Game doesn't work with " + str(numberofdice) + " dice")
