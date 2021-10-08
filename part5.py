shape = input("Enter a shape: ")
s = "square"
r = "rectangle"
c = "circle"
if shape == s:
        l = int(input("What is the length of the square? "))
        print("The area of the square is {}.". format(l**2))
elif shape == r:
    h = int(input("What is the height of the rectangle? "))
    w = int(input("What is the width of the rectangle? "))
    print("The area of the rectangle is {}.". format(h*w))
elif shape == c:
    r = int(input("What is the radius of the circle? "))
    q = input("Enter 'c' for circumference or 'a' for area: ")
    if q == "c":
        print("The circumference is {}.". format(6*r))
    elif q == "a":
        print("The area is {}.". format(3*r**2))
    else:
        print("Invalid choice.")
else:
    print("Invalid shape.")