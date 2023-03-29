# 23 국영수

n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])

'''    
# map 설명
map을 list로 변형하지 않으면 print(b)로 결과를 확인할 수가 없는데 이는 map object가 range()와 비슷하게 필요할 때만 하나씩 꺼내보여주기 때문입니다.

map object의 들어있는 값을 보려면 next()를 이용하면 됩니다.

a = [1,2,3,4,5]
 
b = map(lambda x:x*2, a)
print(next(b))  # 2
print(next(b))  # 4
print(next(b))  # 6
print(next(b))  # 8 
print(next(b))  # 10
print(next(b))  # StopIteration error

# 참고 https://jsp-dev.tistory.com/132

'''    
