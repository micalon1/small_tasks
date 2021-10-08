def ess(a,b):
    l = str(len(a))
    new_string = l + " " + a + b
    return new_string
'''
The Ess function takes two strings as arguments.
It returns the length of the first string followed by a space, and then both strings together as a new single string.
'''
def dess(s, n):
    length_first = int(s[0])
    string1 = s[2:2+length_first]
    string2 = s[2+length_first:]
    if n == 1:
        return string1
    elif n == 2:
        return string2
    else:
        return 'ERROR'
'''
The Dess function takes a string in ESS encoding and an integer that is either 1 or 2 as arguments.
Depending on if the integer is 1 or 2, the function either returns the first or second string from the ESS encoded string.
'''
def echo(s):
    new_s = ""
    for c in s:
        copy = c
        new_s += copy
        new_s += c
    return new_s
def echo(s):            #aaron's solution
    new_s = ""
    for c in s:
        new_s += c + c
    return new_s
'''
The Echo function take a string as an argument.
It returns a new string which each character duplicated.
'''
def find_last_mismatch(s1,s2):
    if s1 == s2:
        return -1
    else:
        tracker = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                tracker = i
    return tracker
def find_last_mismatch(s1,s2):     #aaron's solution
    for i in range(len(s1) -1 , -1, -1): #iterates from end to start (backwards)
        if s1[i] != s2[i]:
            return i
    return -1
'''
The find_last_mismatch function takes two strings as arguments.
It returns the last index where the two strings differ.
'''
def max_length(s1, s2, s3):
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    elif a == b and a == c:
        return a
    elif a > b:
        return a
    elif b > c:
        return b
    elif c > a:
        return c
def max_length(s1, s2, s3):     #aaron's solution
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
'''
The max_length function takes three strings as arguments.
It returns the length of the largest string.
'''
def interleave(one, two, three):
    l = max_length(one,two,three)
    if l != len(one):
        missing1 = " " * (l - len(one))
        one += missing1
    if l != len(two):
        missing2 = " " * (l - len(two))
        two += missing2
    if l != len(three):
        missing3 = " " * (l - len(three))
        three += missing3
    new_string = ""
    s = ""
    for i in range(0,l):
        s = one[i] + two[i] + three[i]
        new_string += s
    return new_string
def interleave(one, two, three):        #aaron's solution
    l = max_length(one,two,three)
    result = ''
    for i in range(l):
        if i >= len(one):
           result += " "
        else:
            result += one[i]
        if i >= len(two):
           result += " "
        else:
            result += two[i]
        if i >= len(three):
           result += " "
        else:
            result += three[i]
    return result
'''
The interleave function takes three strings as arguments.
It returns a new string made up of the first character of each string, then the second character and so forth. If a string is smaller than the maximum length, a space is added for the missing index in the new string.
'''
def get_longest_stretch(string,target):
    counter = 0
    highest = 0
    track = ''
    for c in string:
        if c == target:
            counter += 1
            if counter > highest:
                highest = counter
        else:
            counter = 0
        track = c
    return highest
'''
The get_longest_stretch function take a string and a target character as arguments.
It returns the highest number of times that the target character appears in a row in the string.
'''
def compute_product_at(n,index):
    product = 1
    for e in index:
        product *= n[e]
    return product
'''
The compute_product_at function takes a list of numbers and a list of indexes as arguments.
It returns the product of the values from the first list at the indexes inputted by the second list.
'''
def insert_name_here(vals):
    greater = []
    l = len(vals)
    if l <= 1:
        return []
    else:                           #could also delete first if statement and make else into: if l > 1
        if vals[0] > vals[1]:
            greater.append(vals[0])
        for i in range(1,l-1):
            if vals[i] > vals[i+1] and vals[i] > vals[i-1]:
                greater.append(vals[i])
        if vals[l-1] > vals[l-2]:
            greater.append(vals[l-1])
        return greater
'''
The insert_name_here function take a list of integers as an argument.
It returns a new list with the integers that were greater than the numbers before and after it. The first number is included if it is greater than the integer following it. Similarly, the last number is included if it is greater than the integer before it.
'''
def get_key_to_min(d):
    valid = []
    for key in d:
        if d[key] >= 10:
            valid.append(d[key])
    low = min(valid)
    for k in d:
        if d[k] == low:
            return k
def get_key_to_min(d):          #aaron's solution
    smallest_key = -1
    smallest_val = 1001
    for key in d:
        if d[key] >= 10 and d[key] < smallest_val:
            smallest_key = key
            smallest_val = d[key]
    return smallest_key
'''
The get_key_to_min function takes a dictionary as an argument.
Out of the values in the dictionary that are greater than or equal to 10, the function returns the lowest number.
'''