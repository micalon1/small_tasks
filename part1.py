inch = int(input("Enter number of inches: "))
cent = 2.54*inch
if inch < 0:
    print("ERROR")
else:
    print("Number of centimeters: {}".format(cent))