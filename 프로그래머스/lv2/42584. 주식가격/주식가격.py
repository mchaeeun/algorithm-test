def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        cnt = 0
        j = i + 1
        while j < len(prices):
            cnt += 1
            if prices[i] > prices[j]:
                break
            j += 1
        answer.append(cnt)
    answer.append(0)
    return answer