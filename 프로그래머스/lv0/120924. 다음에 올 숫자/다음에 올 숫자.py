def solution(common):
    i = 0
    r = []

    while len(r) < 2 and i < len(common) - 1:
        if common[i] != 0:
            r.append(common[i+1] / common[i])
        i += 1
    
    if len(r) == 2 and r[0] == r[1]:
        return common[-1] * r[0]
    else:
        d = common[1] - common[0]
        return common[-1] + d