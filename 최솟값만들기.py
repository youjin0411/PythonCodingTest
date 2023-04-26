def solution(A,B):
    answer = 0
    # 내림차순 정렬 
    A.sort()
    # 오름차순 정렬
    B.sort(reverse=True)
    
    for i in range(0, len(A)):
        # 1 * 4 = 4
        # 2 * 4 = 8
        # 4 * 5 = 20
        answer += (A[i] * B[i])
        print(answer)
    return answer