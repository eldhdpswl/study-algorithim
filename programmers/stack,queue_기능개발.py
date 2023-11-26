from collections import deque

def solution(progresses, speeds):
    answer = []

    rest_days = deque()
    for i in range(len(progresses)):
        tmp = 0
        if (100 - progresses[i]) % speeds[i] == 0:
            tmp = (100 - progresses[i]) // speeds[i]
        else:
            tmp = (100 - progresses[i]) // speeds[i] + 1   
        rest_days.append(tmp)

    while rest_days:
        tmp = rest_days.popleft()
        cnt = 1
        while rest_days and tmp >= rest_days[0]:
            rest_days.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
