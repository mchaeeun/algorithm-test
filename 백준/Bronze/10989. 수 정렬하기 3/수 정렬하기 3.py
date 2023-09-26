import sys
n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
sorted_dic = sorted(dic.items())
for x in sorted_dic:
    for i in range(x[1]):
        print(x[0])