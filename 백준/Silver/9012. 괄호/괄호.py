#9012
t = int(input())
for i in range(t):
    s = input()
    vps = "YES"
    sum = 0
    for x in s:
        if x == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    if sum != 0:
        vps = "NO"
    print(vps)