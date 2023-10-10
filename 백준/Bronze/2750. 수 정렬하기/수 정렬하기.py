import sys
from collections import deque
n = int(sys.stdin.readline())
dq = deque()
for i in range(n):
    dq.append(int(sys.stdin.readline()))
dq = sorted(dq)
for i in range(n):
    print(dq[i])