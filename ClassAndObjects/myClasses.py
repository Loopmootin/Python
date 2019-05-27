# counter


class Counter:
    # constructor
    def __init__(self):
        self._value = 0
    # count button method

    def click(self):
        self._value = self._value + 1

    # reset button method
    def reset(self):
        self._value = 0

    # display
    def getValue(self):
        return self._value


# owner


class Owner:
    # constructor
    def __init__(self, ownerid, ownername):
        self._ownerid = ownerid
        self._ownername = ownername

    # get
    def getOwnerid(self):
        return self._ownerid

    def getOwnerName(self):
        return self._ownername

    # toString
    def toString(self):
        return self.getOwnerName() + " has id " + str(self.getOwnerid())


# dog


class Dog:
    # class variable
    _dogcounter = 0

    # constructor
    def __init__(self, dogname="No name yet", owner=None):
        Dog._dogcounter = Dog._dogcounter + 1
        self._dogid = Dog._dogcounter
        self._dogname = dogname
        self._owner = owner

    # get and set
    def getDogid(self):
        return self._dogid

    def getDogName(self):
        return self._dogname

    def getOwner(self):
        return self._owner

    def setDogName(self, name):
        self._dogname = name

    def setOwner(self, owner):
        self._owner = owner

    # toString
    def toString(self):
        return self.getDogName() + " has id " + str(self.getDogid()) + " and owner " + self.getOwner().getOwnerName()
