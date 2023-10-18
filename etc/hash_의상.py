def solution(clothes):
    answer = 1
    category = {}

    for v, k in clothes:
        if k not in category:
            category[k] = 0
        category[k] += 1

    for v in category.values():
        answer *= v + 1
    return answer -1   # -1을 하는 이유는 최소 한 개 이상의 옷을 입어야하므로 모든 종류에서 아무것도 안 입는 경우를 조합한 1을 빼야한다.

