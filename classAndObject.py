from myClasses import Counter
from myClasses import Owner
from myClasses import Dog

# counter example

myCounter = Counter()

myCounter.click()
myCounter.click()

print("Value = " + str(myCounter.getValue()))

myCounter.reset()

print("Value = " + str(myCounter.getValue()))

myCounter.click()

print("Value = " + str(myCounter.getValue()))


# dog and owner example

owner1 = Owner(1, "Jack")
print("First owner = number ", + owner1.getOwnerid(), " :", owner1.getOwnerName())


owner2 = Owner(2, "Jill")
print("Second owner =", owner2.toString())


dog1 = Dog("Fido", owner1)
print(dog1.toString())


dog2 = Dog(owner=owner1, dogname="Fibonacci")
print(dog2.toString())


dog2.setOwner(owner2)
print(dog2.toString())


dog3 = Dog(owner=owner1)
print(dog3.toString())
