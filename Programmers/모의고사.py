def add_o(n):
    return n+1
def solution(answer):
    a = [1, 2, 3, 4, 5]                #수포자1
    b = [2, 1, 2, 3, 2, 4, 2, 5]       #수포자2
    c = [3,3,1,1,2,2,4,4,5,5]          #수포자3

    while True:                     #수포자1의 찍기방식
        for k in range(len(a)):
            a.append(a[k])
            if len(a) == len(answer):
                break
        if len(a) >= len(answer):
            break

    while True:                     #수포자2의 찍기방식
        for k in range(len(b)):
            b.append(b[k])
            if len(b) == len(answer):
                break
        if len(b) >= len(answer):
            break

    while True:                     #수포자3의 찍기방식
        for k in range(len(c)):
            c.append(c[k])
            if len(c) == len(answer):
                break
        if len(c) >= len(answer):
            break


    count1 = 0
    count2 = 0
    count3 = 0
    for x in range(len(answer)):      #정답계산
        if a[x] == answer[x]:
            count1 += 1
        if b[x] == answer[x]:
            count2 += 1
        if c[x] == answer[x]:
            count3 += 1

    count = [count1, count2, count3]  # 수포자 출력용
    large = 0

    if count[0] == count[1] and count[0] == count[2]:           #3명의 정답갯수가 동일할 경우
        return ([1, 2, 3])

    else:

        large: int = max(count)                                 #가장많이 득점한 갯수
        jk = [i for i, value in enumerate(count) if value == large] #인덱스 여러개 찾아오기/ 조건: value가 득점갯수와 동일한거 --->2명이 최고점기록시 2명의 인덱스 뽑음
        jk = list(map(add_o,jk))                                    # jk방은 0,1,2 이니까 1,2,3 으로 보이게 하기위해 사용

        return jk

print(solution([2, 1, 2, 3, 2, 4, 2, 5,1,2,3,4,5,3,3,3,5,5,5,1])) #답안