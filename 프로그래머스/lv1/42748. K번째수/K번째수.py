def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        com = commands[x]
        temp = array[com[0]-1:com[1]]
        temp.sort()
        answer.append(temp[com[2]-1])
    return answer