import sys
from collections import deque

n = int(input())
stack = deque()
message = deque()
for i in range(n):
    message = sys.stdin.readline().split()
    main_message = message[0]
    if main_message == "push":
        stack.append(int(message[1]))
    elif main_message == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif main_message == "size":
        print(len(stack))
    elif main_message == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif main_message == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])