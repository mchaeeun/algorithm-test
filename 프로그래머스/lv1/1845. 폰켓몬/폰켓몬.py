def solution(nums):
    answer = 0
    dic = dict()
    for x in nums:
        if x in dic:
            dic[x] + 1
        else:
            dic[x] = 1
    answer = len(dic.keys())
    if answer > len(nums) // 2:
        answer = len(nums) // 2
    return answer