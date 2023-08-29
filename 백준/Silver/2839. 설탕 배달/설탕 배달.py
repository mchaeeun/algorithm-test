n = int(input())
answer = -1
for i in range(n//3 + 1):
    n_no_three = n - 3 * i
    if n_no_three % 5 == 0:
        answer = n_no_three // 5 + i
        break
print(answer)