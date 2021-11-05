n = 3

count =0
answer = ' '
for x in range(1,n+1):

    if x%2==1:
        #홀수
        answer = answer.replace(' ','수 ')
        count+=1
    else:
        #짝수
        answer = answer.replace(' ', '박 ')
        count+=1
answer = answer.replace(' ','')

print(answer)