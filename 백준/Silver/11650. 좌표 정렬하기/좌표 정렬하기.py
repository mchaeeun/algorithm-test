from collections import deque
import sys

n = int(sys.stdin.readline())
answer = deque()
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    answer.append((x, y))

answer_list = list(answer)
answer_list.sort()

for item in answer_list:
    print(item[0], item[1])