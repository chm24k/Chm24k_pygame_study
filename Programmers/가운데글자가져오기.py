
s = 'abcdde'

k = len(s)//2
if len(s)%2== 1:
    #홀수
    answer = s[k]
else:
    #짝수
    answer = s[k-1:k+1]

print(answer)