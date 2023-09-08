import sys
n = int(input())
input_line1 = sys.stdin.readline().strip()
a = set(map(int, input_line1.split()))
m = int(sys.stdin.readline())
input_line2 = sys.stdin.readline().strip()
numbers = list(map(int, input_line2.split()))
for x in numbers:
    if x in a:
        print(1)
    else:
        print(0)