n = int(input()) - 1
answer = 0
while n > 0:
    answer += 1
    n -= 6 * answer
print(answer + 1)