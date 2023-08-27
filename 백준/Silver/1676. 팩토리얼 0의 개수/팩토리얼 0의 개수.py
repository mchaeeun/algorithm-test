def count(a, q):
    answer = 0
    while q % a == 0:
        answer += 1
        q /= a
    return answer

n = int(input())
count_two = 0
count_five = 0

if n < 5:
    pass
else:
    for x in range(2, n+1):
        count_two += count(2, x)
        count_five += count(5, x)

print(min(count_two, count_five))