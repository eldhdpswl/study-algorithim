# 큰수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰수 더하는 횟수
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second  # 두번째로 큰수 더하기
 
print(result)
