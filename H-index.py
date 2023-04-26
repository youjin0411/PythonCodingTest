def solution(citations):
    # 내림차순 정렬 [6, 5, 3, 1, 0]
    citations.sort(reverse=True)
    # enumerate는 리스트의 인덱스와 값이 튜플 형태로 리턴 
    # 즉 enumerate의 인덱스는 처음 변수는 idx,
    # 값은 citaion에 들어간다. 
    for idx , citation in enumerate(citations):
        # 만약 citation보다 idx 인덱스가 크거나 같으면 인덱스 리턴 
        if idx >= citation:
            return idx
    return len(citations)