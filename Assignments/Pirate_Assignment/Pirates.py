# owner


class Pirate:
    # constructor
    def __init__(self, name, pointer=None):
        self._name = name
        self._pointer = pointer

    # get
    def getName(self):
        return self._name

    def getPointer(self):
        return self._pointer

    def setPointer(self, pointer):
        self._pointer = pointer

    # toString
    def toString(self):
        return self.getName() + " points to " + self.getPointer()
