import sys
from collections import deque

n = int(sys.stdin.readline())
input_stack = deque()
result_stack = deque()
answer = deque()
for i in range(n):
    input_stack.append(int(sys.stdin.readline()))
i = 1

while input_stack:
    tmp = input_stack.popleft()
    while i <= tmp:
        result_stack.append(i)
        answer.append('+')
        i += 1
    while len(result_stack) > 0:
        answer.append('-')
        cur = result_stack.pop()
        if cur == tmp:
            break
        else:
            print("NO")
            exit()

while answer:
    print(answer.popleft())