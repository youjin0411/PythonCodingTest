data = []
for i in range(1, 11):
    data.append(i)
    
[i for i in range(1, 11)]

# 짝수와 5의 배수가 동시에 만족하는 경우 
[i for i in range(11) if i % 2 == 0 if i % 5 == 0]