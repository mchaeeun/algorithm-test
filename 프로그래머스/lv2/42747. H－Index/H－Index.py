def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            break
        else:
            answer += 1
    return answer