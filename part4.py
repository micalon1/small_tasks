target=int(input("Enter target number: "))
start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))
if target < end and target >= start:
    print("Within range!")
else:
    print("Not within range...")