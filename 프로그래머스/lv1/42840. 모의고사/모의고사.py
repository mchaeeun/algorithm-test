def solution(answers):
    answer = []
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thi = [3,3,1,1,2,2,4,4,5,5]
    soopo = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == fir[i%len(fir)]:
            soopo[0] += 1
        if answers[i] == sec[i%len(sec)]:
            soopo[1] += 1
        if answers[i] == thi[i%len(thi)]:
            soopo[2] += 1
    maximum = max(soopo)
    for i in range(len(soopo)):
        if maximum == soopo[i]:
            answer.append(i+1)
    return answer