# 입국심사

def solution(n, times):
    answer = 0

    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time
            if checked >= n:
                break

        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked <= n:
            left = mid + 1

    return answer  


# 참고출처
# https://happy-obok.tistory.com/10
# https://sohee-dev.tistory.com/123
