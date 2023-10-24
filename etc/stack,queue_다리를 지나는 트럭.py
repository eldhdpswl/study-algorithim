#다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    currentweight = 0
    while len(truck_weights) != 0:
        time += 1
        currentweight -= bridge.popleft()

        if currentweight + truck_weights[0] <= weight:
            currentweight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    time += bridge_length #브릿지 큐에 방금 마지막 트럭이 들어갔으므로, 브릿지 길이만큼 더해줘야함

    return time 


#참고출처
#https://jie0025.tistory.com/428
#https://this-programmer.tistory.com/372
