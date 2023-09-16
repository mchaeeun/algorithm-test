import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
answer = 8 * 8
dq = deque()

for i in range(n):
    dq.append(sys.stdin.readline().strip())
    
for i in range(n - 7):
    for j in range(m - 7):
        a = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                q = 0
                if (k + l) % 2 == 0:
                    if dq[k][l] == 'W':
                        a += 1
                else:
                    if dq[k][l] == 'B':
                        a += 1
        a = min(a, 8*8 - a)
        answer = min(a, answer)

print(answer)