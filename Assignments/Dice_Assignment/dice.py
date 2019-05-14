# red_die = [0, 0, 4, 4, 8, 8]
# green_die = [2, 2, 3, 3, 7, 7]
# blue_die = [1, 1, 5, 5, 6, 6]


class Die:
    # constructor
    def __init__(self, color, sides, scores):
        self._color = color
        self._sides = sides
        self._scores = scores

    # get
    def getColor(self):
        return self._color

    def getSides(self):
        return self._sides

    def getScores(self):
        return self._scores

    # toString
    def toString(self):
        return self._color + " die has the sides " + str(self._sides)
        + " and an empty score list " + str(self._scores)