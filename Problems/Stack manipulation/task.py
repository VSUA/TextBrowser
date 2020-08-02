from collections import deque

count_of_actions = int(input())
numbers = deque()

for _ in range(count_of_actions):
    action = input().split()
    if action[0] == "PUSH":
        numbers.append(action[1])
    else:
        numbers.pop()

for _ in range(len(numbers)):
    print(numbers.pop())
