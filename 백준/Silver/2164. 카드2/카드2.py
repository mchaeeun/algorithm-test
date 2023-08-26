#2164
import sys
from collections import deque
n = int(sys.stdin.readline())
#n = int(input())
card = deque()
for i in range(n):
    card.append(i+1)
while len(card) != 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0])