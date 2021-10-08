first=input("Enter first word: ")
sec=input("Enter second word: ")
third=input("Enter third word: ")
b="blah"
if first==b and sec!=b and third!=b:
    print("The word \"blah\" was entered 1 time. That\'s great.")
elif first!=b and sec==b and third!=b:
    print("The word \"blah\" was entered 1 time. That\'s great.")
elif first!=b and sec!=b and third==b:
    print("The word \"blah\" was entered 1 time. That\'s great.")
elif first==b and sec==b and third!=b:
    print("The word \"blah\" was entered 2 times. That\'s great.")
elif first==b and third==b and sec!=b:
    print("The word \"blah\" was entered 2 times. That\'s great.")
elif sec==b and third==b and first!=b:
    print("The word \"blah\" was entered 2 times. That\'s great.")
elif first==b and sec==b and third==b:
    print("The word \"blah\" was entered 3 times. That\'s great.")
else:
    print("The word \"blah\" was entered 0 times. That\'s great.")