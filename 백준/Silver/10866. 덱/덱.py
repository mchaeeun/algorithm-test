from collections import deque
import sys

main_deque = deque()

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()
    main_command = command[0]
    if main_command == "push_front":
        main_deque.appendleft(command[1])
    elif main_command == "push_back":
        main_deque.append(command[1])
    elif main_command == "pop_front":
        if len(main_deque) == 0:
            print(-1)
        else:
            print(main_deque.popleft())
    elif main_command == "pop_back":
        if len(main_deque) == 0:
            print(-1)
        else:
            print(main_deque.pop())
    elif main_command == "size":
        print(len(main_deque))
    elif main_command == "empty":
        if len(main_deque) == 0:
            print(1)
        else:
            print(0)
    elif main_command == "front":
        if len(main_deque) == 0:
            print(-1)
        else:
            print(main_deque[0])
    elif main_command == "back":
        if len(main_deque) == 0:
            print(-1)
        else:
            print(main_deque[-1])