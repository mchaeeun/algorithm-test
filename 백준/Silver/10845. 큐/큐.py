from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()
    main_command = command[0]
    if main_command == "push":
        queue.append(int(command[1]))
    elif main_command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif main_command == "size":
        print(len(queue))
    elif main_command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif main_command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif main_command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])