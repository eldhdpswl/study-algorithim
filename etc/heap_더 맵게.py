# 더 맵게

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)

    count = 0

    while len(scoville) > 1:
        
        first = heapq.heappop(scoville)

        if first < k:
            count += 1
            second = heapq.heappop(scoville)

            heapq.heappush(scoville, (first + (second * 2)))
        else:
            break

    return -1 if scoville[0] < k else count  


#참고출처
# https://aiday.tistory.com/109
# https://mini-min-dev.tistory.com/202
# https://littlefoxdiary.tistory.com/3 # 힙 설명
