def solution(survey, choices):
    answer = 'RCJA'
    g1 = ["RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA"];
    score = [3, 2, 1, 0,-1, -2, -3];
    totalscore = [0, 0, 0, 0, 0, 0, 0, 0];
    
    for i in range(0, len(survey)):  # 0 ~ survery.length-1번 반복 
        res = g1.index(survey[i])  #g1 배열안에서 survey 인덱스 구하기 
        totalscore[res] += score[choices[i]-1]; #totalscore[res] 자리에 점수를 더한다.
        
    for i in totalscore:
        print(i)
    if totalscore[0] < totalscore[1]: answer = answer.replace('R', 'T')
    if totalscore[2] < totalscore[3]: answer = answer.replace('C', 'F')
    if totalscore[4] < totalscore[5]: answer = answer.replace('J', 'M')
    if totalscore[6] < totalscore[7]: answer = answer.replace('A', 'N')
    return answer

answer = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]	)
print(answer)