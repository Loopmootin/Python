from Pirates import Pirate


treasureGameNumber = 4

PD = Pirate("Dummy")
P1 = Pirate("Torsten Træben")
P2 = Pirate("Kenny Klap For Øjet")
P3 = Pirate("Per Papegøje")
P4 = Pirate("Verner Veganer")

listOfPirates = ['PD', 'P1', 'P2', 'P3', 'P4']

PD.setPointer(P1._name)
P1.setPointer(P2._name)
P2.setPointer(P3._name)
P3.setPointer(PD._name)

print("The first pirate is called", PD.getName(), " and he points to pirate ", PD.getPointer())
print("The first pirate is called", P1.getName(), " and he points to pirate ", P1.getPointer())
print("The first pirate is called", P2.getName(), " and he points to pirate ", P2.getPointer())
print("The first pirate is called", P3.getName(), " and he points to pirate ", P3.getPointer())
print("The first pirate is called", P4.getName(), " and he points to pirate ", P4.getPointer())
print()

print(len(listOfPirates))
print()

listLength = len(listOfPirates)

for p in range(listLength):
    if Pirate.getPointer is None:
        print("Jeg peger fucking ikke på nogen")
    else:
        print("Jeg fucking peger på dig")
print()