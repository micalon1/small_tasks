def subtract_eight(n):
    return (n - 8)
# def foo(first_string, first_i, sec_string, sec_i):
#     try:
#         if first_string[first_i] == sec_string[sec_i]:
#             return True
#         else:
#             return False
#     except:
#         return False

def foo(first_string, first_i, sec_string, sec_i):
    if first_i >= len(first_string) or sec_i >= len(sec_string): #if out of range --> prevents crash
        return False
    return first_string[first_i] == sec_string[sec_i]

def repeats_same(s):
    letter = ''
    for c in s:
        if c == letter:
            return True
        letter = c
    return False
