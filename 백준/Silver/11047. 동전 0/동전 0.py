import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
coins = deque()
count = 0
for i in range(n):
    coins.append(int(sys.stdin.readline()))

while k > 0:
    coin = coins.pop()
    count += k // coin
    k %= coin
print(count)