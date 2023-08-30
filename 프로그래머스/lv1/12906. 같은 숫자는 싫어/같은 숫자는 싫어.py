def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for x in arr:
        if len(answer) == 0:
            answer.append(x)
        else:
            if answer[-1] != x:
                answer.append(x)
    return answer