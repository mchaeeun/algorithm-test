def solution(participant, completion):
    participant.sort()
    completion.sort()
    i = 0
    while len(completion) > i:
        if participant[i] != completion[i]:
            return participant[i]
        i += 1
    return participant[-1]
    