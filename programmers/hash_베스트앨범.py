def solution(genres, plays):
    answer = []
    
    index = {}
    score = {}

    for i,  (genre, play) in enumerate(zip(genres, plays)):
        if genre not in index:
            index[genre] = [(i, play)]
        else:
            index[genre].append((i, play))

        if genre not in score:
            score[genre] = play
        else:
            score[genre] += play

    for (k, y) in sorted(score.items(), key=lambda x:x[1], reverse=True):
        for (i, play) in sorted(index[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer        

# 재생횟수 기준 내림차순, 고유번호 기준 오름차순 정렬
# 딕셔너리에 items() 메서드를 사용해주면 {"key" : value}의 형태를 [(key, value)]의 형태로 만들어 준다.
  
    
#genres=["classic", "pop", "classic", "classic", "pop"]
#plays=[500, 600, 150, 800, 2500]
#print(solution(genres, plays))
