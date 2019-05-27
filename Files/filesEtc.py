import pickle
from classes import Owner
from classes import Dog


# write and read a text file

outfile = open("mytextfile", "w")
outfile.write(str(6.0) + "\n")
outfile.write(str(7.3) + "\n")
outfile.write(str(12.0) + "\n")
outfile.close()

infile = open("mytextfile", "r")
line = infile.readline()

while line != "":
    value = float(line)
    print(value)
    line = infile.readline()

infile.close()


# write and read a single object

owner1 = Owner(1, "Jack")

oneownerfile = open("oneowner", "wb")
pickle.dump(owner1, oneownerfile)
oneownerfile.close()

oneownerfile = open("oneowner", "rb")
newowner1 = pickle.load(oneownerfile)

print(newowner1.toString())
print("--------------------")


# write and read a list of objects

owner1 = Owner(1, "Jack")
owner2 = Owner(2, "Jill")

ownerlist = []

ownerlist.append(owner1)
ownerlist.append(owner2)

listownerfile = open("listowner", "wb")
pickle.dump(ownerlist, listownerfile)
listownerfile.close

listownerfile = open("listowner", "rb")
newownerlist = pickle.load(listownerfile)

for i in range(len(newownerlist)):
    print(newownerlist[i].toString())
print("--------------------")


# list of objects with references

owner1 = Owner(1, "Jack")
owner2 = Owner(2, "Jill")

ownerlist = []

ownerlist.append(owner1)
ownerlist.append(owner2)


dog1 = Dog("Fido", owner1)
dog2 = Dog("Pluto", owner2)
dog3 = Dog(dogowner=owner1)

doglist = []

doglist.append(dog1)
doglist.append(dog2)
doglist.append(dog3)


objectlist = []

objectlist.append(ownerlist)
objectlist.append(doglist)


dogownerfile = open("listdogowner", "wb")
pickle.dump(objectlist, dogownerfile)
dogownerfile.close

dogownerfile = open("listdogowner", "rb")
newobjectlist = pickle.load(dogownerfile)

newownerlist = newobjectlist[0]
for i in range(len(newownerlist)):
    print(newownerlist[i].toString())
print()

newdoglist = newobjectlist[1]
for i in range(len(newdoglist)):
    print(newdoglist[i].toString())
print("--------------------")
