# 7. 리스트에서 특정 원소만 추출하기
#직접만든것
#ex) [1,2,2,2,3,1,1,3,2]에서 2를 제외한 나머지만 추출하기
#
# list = [1,2,2,2,3,1,1,3,2]
# result = []
# for x in range(0,int(len(list))):
#     if list[x] != 2:
#         result+=str(list[x])
#
# for x in result:
#     print(x,end = ' ')


#------------------------------------------------------

#일반적인 방법
#방법1

arr = [1,2,2,2,3,1,1,3,2]
result = list()
for x in arr:
    if x !=2:
        result.append(x)
print(result) #결과(2를 제외한것)
print(arr) #변하지 않음

#------------------------------------------------------

#방법2 (***너무 위험해서 안쓰는걸 추천***) (리스트 자체를 바꾸는건 위험) (************비추*******)

# 반복횟수 = arr.count(2) #2가 몇개인지확인
# for i in range(반복횟수):
#     #2를 지운다
#     arr.remove(2)
#
# print(arr)