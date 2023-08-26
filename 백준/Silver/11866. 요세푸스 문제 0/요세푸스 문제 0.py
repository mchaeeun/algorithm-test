#11866
from collections import deque
n, k = map(int, input().split())
list = [ i + 1 for i in range(n) ]
answer = deque()
i = 0
for x in range(len(list)):
    i = (i + k - 1) % len(list)
    answer.append(list[i])
    del list[i]
formatted_list = "<" + ", ".join(map(str, answer)) + ">"
print(formatted_list)