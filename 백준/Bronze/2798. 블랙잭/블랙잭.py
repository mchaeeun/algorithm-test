import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
tmp = 0

for i in range(0, n - 2):
    for j in range(i+1, n - 1):
        for k in range(j+1, n):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp <= m and tmp > result:
                result = tmp
print(result)