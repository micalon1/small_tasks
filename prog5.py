def count_in_other(list1, list2):
    counter = 0
    for e in range(len(list2)):
        if list2[e] in list1:
            counter += 1
    return counter

def positive_values(d):
    for k in d:
        if d[k] <= 0:
            return False
def buy_items(dict1, dict2, dict3):
    total = 0
    if positive_values(dict1) == False or positive_values(dict2) == False or positive_values(dict3) == False:
        return -1
    for i in dict1:
        if i not in dict3:
            return -2
    for i in dict2:
        if i in dict1 and dict2[i] <= dict1[i]:
            total += (dict3[i] * dict2[i])
        else:
            return -3
    return total

def count_less_than(list1, k):
    counter = 0
    for element in list1:
        for n in element:
            if n == 0:
                return -1
            elif n < k:
                counter += 1
    return counter

def count_absences(seating_chart, attendance):
    count = 0
    for row in range(len(seating_chart)):
        if seating_chart[row] != attendance[row]:
            for name in range(len(seating_chart[row])):
                if seating_chart[row][name] != attendance[row][name]:
                    count += 1
    return count

def find_in_other(list1, list2):
    group = []
    for number in list1:
        inner_group = []
        if number in list2:
            for i in range(len(list2)):
                if list2[i] == number:
                    inner_group.append(i)
        else:
            inner_group += ''
        group.extend([inner_group])
    return group

def count_has_k_even_divisors(n, k):
    counter = 0
    for integer in range(1,n+1):
        track = 0
        for divisor in range(1, integer+1):
            if integer % divisor == 0:
                track += 1
        if track == k:
            counter += 1
    return counter