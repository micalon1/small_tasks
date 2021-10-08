sec=int(input("Enter number of seconds: "))
mins=sec//60
over=sec%60
if mins==1 and over==1:
    print("That is {} minute and {} second.".format(mins,over))
elif over==1:
    print("That is {} minutes and {} second.".format(mins,over))
elif mins==1:
    print("That is {} minute and {} seconds.".format(mins,over))
else:
    print("That is {} minutes and {} seconds.".format(mins,over))