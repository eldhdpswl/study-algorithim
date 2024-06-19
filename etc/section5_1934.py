# 유클리드 호제법
# 최대 공약수를 구한 후, 두 수의 곱에서 최대 공약수를 나눠 주는 것으로 해결
# A * B / 최대공약수 => 최소공배수

t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)   # 큰수 작은수 순서는 자연스럽게 swap이 된다.

for i in range(t):
    a, b = map(int, input().split()) 
    result = a*b / gcd(a, b)
    print(int(result))
