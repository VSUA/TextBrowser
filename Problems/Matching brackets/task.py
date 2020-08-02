from collections import deque

string = input()
brackets = deque()
try:
    for char in string:
        if char == "(":
            brackets.append(char)
        elif char == ")":
            brackets.pop()
    if len(brackets) == 0:
        print("OK")
    else:
        print("ERROR")
except IndexError:
    print("ERROR")

