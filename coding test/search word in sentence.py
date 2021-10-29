# 6. 어떤 문자열에 해당언어가 몇개 있는지 카운팅
# ex) "ILOVKEFLOVEE"에서 "LOV"가 몇개 있는지 카운팅
import re

sentence = 'ILOVKEFLOVEE'
search = 'LOV'
count = int(len(re.findall(search,sentence)))  # re.findall('찾을문자','문장')


print(f'문장 |  {sentence}')
print(f'-'*20)
print(f'{search}는 {count}번 들어갔습니다')



#-----------------------------------------------------------
# 박지우 선생님 pick

string = "LOVELO"
find = "LOV"
count2 = 0

#01. 왜 일반화된 코드가 아닐까?   ==>   find 문자열의 길이에 따라 코드가 달라짐
#02. 결함을 찾아라   ==>   string의 index범위를 넘어설 수 있다.
for i in range(len(string)):  # Q2결함
    if string[i] =="L" and i+len(find) <= len(string):
        if string[i+1] == 'O':
            if string[i+2] == 'V':
                count2 +=1


print(f'\n','-'*20,'\n박지우 선생님 pick')
print(count2)
