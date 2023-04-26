def solution(s):
    answer = ''
    # " " 공백을 기준으로 문자를 자른다. 
    s = s.split(" ")
    # 공백을 기준으로 자른 문자열의 배열을 순회
    for i in range(0, len(s)):
        # capitalize() 함수는 첫 글자를 대문자로 만들어준다. 
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer