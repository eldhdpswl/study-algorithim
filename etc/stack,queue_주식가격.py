# 주식가격

from collections import deque

def solution(prices):
    result = []
    queue = deque(prices)

    while queue:
        period = 0
        price = queue.popleft()

        for after in queue:
            period += 1
            if price > after:
                break
        result.append(period)

    return result


prices = [1, 2, 3, 2, 3]

solution(prices)


#참고출처
# https://aiday.tistory.com/100
# https://deftkang.tistory.com/175
# https://tngusmiso.tistory.com/34
