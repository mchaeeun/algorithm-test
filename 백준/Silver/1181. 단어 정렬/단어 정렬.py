import sys
from collections import deque

answer = deque()
n = int(sys.stdin.readline())
for i in range(n):
    answer.append(sys.stdin.readline().strip())
answer = list(set(answer))
answer.sort()
answer.sort(key=len)
for x in answer:
    print(x)