import sys
n = int(input())
input_line = sys.stdin.readline().strip()
numbers = list(map(int, input_line.split()))
answer = 0
for x in numbers:
    if x == 1:
        continue
    else:
        found = False
        for i in range(2,x):
            if x % i == 0:
                found = True
                break
        if found == False:
            answer += 1
print(answer)