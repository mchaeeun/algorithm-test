answer = 1
n, k = map(int, input().split())
for x in range(k):
    answer *= n - x
for x in range(k):
    answer /= x + 1
print(int(answer))