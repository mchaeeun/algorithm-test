import sys
import math
t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    if floor == 0:
        floor = h
    print('{:d}{:02d}'.format(floor, math.ceil(n/h)))