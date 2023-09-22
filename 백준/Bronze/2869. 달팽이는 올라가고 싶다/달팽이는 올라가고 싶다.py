import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
day = (v - a) / (a - b) + 1
print(math.ceil(day))