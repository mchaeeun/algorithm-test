import sys
from collections import deque

n = int(sys.stdin.readline())
sg_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find_cards = list(map(int, sys.stdin.readline().split()))
dic_cards = dict()
answer = deque()

for x in sg_cards:
    if x in dic_cards:
        dic_cards[x] += 1
    else:
        dic_cards[x] = 1

for y in find_cards:
    if y in dic_cards:
        print(dic_cards[y], end=" ")
    else:
        print(0, end=" ")