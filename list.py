# Lists

listoftext = ['one', 'two', 'three']
listofnumbers = [1, 2, 3]
listmixed = listoftext + listofnumbers

listempty = []

print(listoftext)
print(listofnumbers)
print(listmixed)
print(listmixed[2:4])  # no logic
print(listmixed[-2])  # no logic

print(listempty)

listoftext.append('four')
print(listoftext)

listoftext.insert(1, 'oneandahalf')
print(listoftext)

del listoftext[4]
print(listoftext)

print("Removed: ", listoftext.pop(0))
print(listoftext)

for i in range(len(listoftext)):
    if(i > 0):
        print(" | ", end="")
    print(listoftext[i], end="")
print()
print()


# Tuple

GRADES = (-3, 00, 2, 4, 7, 10, 12)

print(GRADES)
print()
