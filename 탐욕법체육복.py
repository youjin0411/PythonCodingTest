def solution(n, lost, reserve):
    # 현재 체육을 할 수 있는 학생의 수 
    answer = n - len(lost)
    # 순서대로 정렬을 해 주어야지, 시간초과 문제가 발생하지 않는다. 
    lost.sort()
    reserve.sort()
    # 여분 체육복을 가져온 학생이 체육복 도난 당함.
    for i in range(0, len(reserve)):
        for j in range(0, len(lost)):
            if reserve[i] == lost[j]:
                # 체크 
                reserve[i] = -1
                # 체크
                lost[j] = -1
                # 체육복을 빌려줄 수 있으므로, answer+=1
                answer+=1
                break
    # 체육복 빌리기
    for i in range(0, len(reserve)):
        for j in range(0, len(lost)):
            # 여분 체육복을 가져온 학생이 체육복을 도난 당한 학생의 앞번호이거나, 뒷번호이면
            if (reserve[i] == lost[j]+1) or (reserve[i] == lost[j] - 1):
                answer+=1
                # 체크 
                reserve[i] = -1
                # 체크
                lost[j] = -1
                break
    return answer

ans = solution(5, [2, 4], [1, 3, 5])
print(ans)