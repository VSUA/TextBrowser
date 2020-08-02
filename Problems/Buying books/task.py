from collections import deque

n = int(input())

books = deque()
read_books = deque()

for _ in range(n):
    action = input().split(" ", 1)
    if action[0] == "READ":
        read_books.append(books.pop())
    else:
        books.append(action[1])

for _ in range(len(read_books)):
    print(read_books.pop())