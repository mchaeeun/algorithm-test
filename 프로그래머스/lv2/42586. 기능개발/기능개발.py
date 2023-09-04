def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            day = 1
            del progresses[0]
            del speeds[0]
            while len(progresses) != 0 and progresses[0] >= 100:
                day += 1
                del progresses[0]
                del speeds[0]
            answer.append(day)
    return answer