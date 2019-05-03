from flask import Flask, render_template, request, Markup

app = Flask(__name__)

# GET the first time.
@app.route('/', methods=['GET'])
def hello():
    global mytitle, gamehistory, experience, pile, currentgame, computerwin, mydisabled
    return render_template('Nim.html', title=mytitle, history=gamehistory)


@app.route('/', methods=['POST'])
def play():
    global mytitle, gamehistory, experience, pile, currentgame, computerwin, mydisabled
    if request.form['myaction'] == 'Send':
        # Take from pile, no input check.
        taken = int(request.form['mytake'])
        pile = pile - taken
        currentgame[pile] = -1
        gamehistory.append(Markup("You took " + str(taken) + "; " + str(pile) + " left"))
        # Computermove.
        computermove()
    else:
        resetgame()
    return render_template('nim.html', title=mytitle, history=gamehistory, disabled=mydisabled)


def computermove():
    global mytitle, gamehistory, experience, pile, currentgame, computerwin, mydisabled
    if pile == 0:
        gamehistory.append(Markup("You win!"))
        updateexperience()
    else:
        # Take a number, max 3, min 1, max number in pile
        if pile >= 3 and experience[pile - 3] > experience[pile - 1] and experience[pile - 3] > experience[pile - 2]:
            taken = 3
        elif pile >= 2 and experience[pile - 2] > experience[pile - 1]:
            taken = 2
        else:
            taken = 1
        pile = pile - taken
        currentgame[pile] = 1
        gamehistory.append(Markup("Computer took " + str(taken) + "; " + str(pile) + " left"))
        if pile == 0:
            gamehistory.append(Markup("Computer wins!"))
            computerwin = True
            updateexperience()


def updateexperience():
    global mytitle, gamehistory, experience, pile, currentgame, computerwin, mydisabled
    mydisabled = 'disabled'
    for i in range(1, 22):
        if computerwin:
            experience[i] += currentgame[i]
        else:
            experience[i] -= currentgame[i]
    experience[i] = min(10, experience[i])
    experience[i] = max(-10, experience[i])
    # Print in log
    print(currentgame)
    print(experience)


# Reset game.
def resetgame():
    global mytitle, gamehistory, experience, pile, currentgame, computerwin, mydisabled
    mytitle = "Nim with one pile"  # Global title.
    pile = 21  # Nr of items in pile.
    currentgame = [0] * 22  # The current game, that is on the board.
    gamehistory = []  # Sets gamehistory to a empty list; for saveing the history of the game.
    # Markup is needed to display a string as HTML with e.g. &nbsp;
    gamehistory.append(Markup("You start : " + str(pile) + " items in pile"))
    computerwin = False
    mydisabled = ""  # Disabled button.


experience = [0] * 22
experience[0] = 11
resetgame()

#####
if __name__ == '__main__':
    app.run('localhost', 4449)
