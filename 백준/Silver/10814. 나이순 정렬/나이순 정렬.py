import sys
from collections import deque

n = int(sys.stdin.readline())
dic = dict()
for i in range(n):
    age, name = sys.stdin.readline().split()
    if int(age) not in dic:
        dic[int(age)] = deque()
    dic[int(age)].append(name)
answer = sorted(dic.items())

for key, value in answer:
    for item in value:
        print(key, item)