
line = "Mary    had a little     lamb,"
print(line)
print()

wordlist = line.split()

for word in wordlist:
    newword = word.rstrip(',')
    print(newword)
print()

print("The line starts with", line[0])
print()

upperline = line.upper()
print(upperline)
print()

print(line.replace("little", "big"))
print()

print("little" in line)
print()

print("a =", line.count("a"))
print()

newline = line.replace("    ", " ")
newline = newline.replace("     ", " ")

print(newline)
print()