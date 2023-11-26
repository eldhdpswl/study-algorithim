# 단어변환

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft()

        if x == target:
            return cnt
        
        for i in range(0, len(words)):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, cnt + 1])
    return 0


# 참고출처
# https://reliablecho-programming.tistory.com/115
# https://naa0.tistory.com/153#2.1.%20%EC%BD%94%EB%93%9C
