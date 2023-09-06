import sys
from collections import deque

n = int(sys.stdin.readline())
before_answer = deque()
for i in range(n):
    x = int(sys.stdin.readline())
    before_answer.append(x)

set_answer = set(before_answer)
answer = list(set_answer)
answer.sort()

for i in range(len(answer)):
    print(answer[i])