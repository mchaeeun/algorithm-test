import sys
from collections import deque

CLOSE = [')', ']']

for line in sys.stdin:
    if line == "." or line == '.\n':
        break
    dq = deque()
    answer = "yes"
    for char in line:
        if char == '(':
            dq.append(')')
        elif char == '[':
            dq.append(']')
        elif char not in CLOSE:
            continue
        elif len(dq) == 0 or char != dq.pop():
            answer = "no"
            break
    if len(dq) != 0:
        answer = "no"
    print(answer)
