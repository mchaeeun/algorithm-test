import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 < K:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + 2 * min2)
            answer += 1
        else:
            break
    if scoville[0] < K:
        return -1
    else:
        return answer