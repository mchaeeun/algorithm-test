def solution(n):
    answer = 0
    for x in range(n):
        answer += 1
        while answer % 3 == 0 or answer % 10 == 3 or (answer // 10) % 10 == 3:
            answer += 1
    return answer