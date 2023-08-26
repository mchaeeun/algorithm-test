import sys
s = sys.stdin.readline().rstrip('\n')
while s != "0":
    answer = "yes"
    while len(s) > 1:
        if s[0] != s[-1]:
            answer = "no"
            break
        else:
            s = s[1:-1]
    print(answer)
    s = sys.stdin.readline().rstrip('\n')