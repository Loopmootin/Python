# try/except/finally

done = False
mylist = ['a', 'b', 'c', 'd', 'e']

while not done:
    try:
        number = int(input("Write an integer:"))
        print("You chose:", mylist[number])
    except ValueError:  # Error: A specific error - If we do not enter an integer (should always come first)
        print("Not an integer")
    except Exception as ex:  # Error: General - Should always be last.
        print("Exception:", ex)
    finally:
        done = bool(input('Done ? (return is "no" (False), any other answer is "yes" (True)):'))
print("Done")