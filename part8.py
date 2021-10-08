s = ""
enter = ""
total = ""
z = ""
while s != "Done":
    s = input("Enter string: ")
    if s != "Done":
        enter = s + enter
        total = "Done" + enter
if s == "Done" or enter == "Done":
    total = "Done" + enter
    print(total)