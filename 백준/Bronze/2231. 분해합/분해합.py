import sys
n = int(sys.stdin.readline())
m = n - len(str(n)) * 9
while m < n:
    tmp = m
    divsum = tmp
    while tmp > 0:
        divsum += tmp % 10
        tmp //= 10
    if n == divsum:
        break
    m += 1
if m == n:
    print(0)
else:
    print(m)