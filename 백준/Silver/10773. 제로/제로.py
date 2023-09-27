import sys
from collections import deque
k = int(sys.stdin.readline())
dq = deque()
for i in range(k):
    x = int(sys.stdin.readline())
    if x == 0:
        dq.pop()
    else:
        dq.append(x)
print(sum(dq))