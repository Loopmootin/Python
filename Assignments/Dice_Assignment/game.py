import random

red_die = [0, 0, 4, 4, 8, 8]
green_die = [2, 2, 3, 3, 7, 7]
blue_die = [1, 1, 5, 5, 6, 6]

red_die_list = []
green_die_list = []
blue_die_list = []


def roll_die_2():
    i = 0
    num = numberofrolls

    if(choose_player1 == 1):
        first_player = red_die
        first_player_list = red_die_list
    elif(choose_player1 == 2):
        first_player = green_die
        first_player_list = green_die_list
    else:
        first_player = blue_die
        first_player_list = blue_die_list

    if(choose_player2 == 1):
        second_player = red_die
        second_player_list = red_die_list
    elif(choose_player2 == 2):
        second_player = green_die
        second_player_list = green_die_list
    else:
        second_player = blue_die
        second_player_list = blue_die_list

    while i < num:
        roll1 = random.choices(first_player)[0]
        roll2 = random.choices(second_player)[0]
        if(roll1 > roll2):
            first_player_list.append("+")
        else:
            second_player_list.append("+")
        i = i + 1


def roll_die_3():
    i = 0
    num = numberofrolls

    while i < num:
        roll1 = random.choices(red_die)[0]
        roll2 = random.choices(green_die)[0]
        roll3 = random.choices(blue_die)[0]
        if(roll1 > roll2 and roll1 > roll3):
            red_die_list.append("+")
        elif(roll2 > roll1 and roll2 > roll3):
            green_die_list.append("+")
        elif(roll3 > roll1 and roll3 > 2):
            blue_die_list.append("+")
        i = i + 1


numberofdice = int(input("Choose number of players(2 or 3): "))
numberofrolls = int(input("Choose number of rolls: "))

if(numberofdice == 2):
    first_player = int(input("Choose first player with number [1, 2, 3]: "))
    sescond_player = int(input("Choose second player with number [1, 2, 3]: "))

    roll_die_2()
    first_length = len(first_player_list)
    second_length = len(second_player_list)

    print(str(first_player) + " : " + str(first_length))
    print(str(sescond_player) + " : " + str(second_length))

elif(numberofdice == 3):
    choose_player1 = 1
    choose_player2 = 2
    choose_player3 = 3

    roll_die_3()
    red_length = len(red_die_list)
    green_length = len(green_die_list)
    blue_length = len(blue_die_list)

    print(str(red_die) + " : " + str(red_length))
    print(str(green_die) + " : " + str(green_length))
    print(str(blue_die) + " : " + str(blue_length))

else:
    print("Game doesn't work with " + numberofdice + " dice")
