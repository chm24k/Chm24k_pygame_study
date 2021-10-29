# 버블소트 (bubble sort)

arr = [4,3,2,7,9]
arr_save = [0,0,0,0,0]

while(True):
    for x in range(len(arr)-1):
        # if x ==4:         #위에 (len(arr)) 이었다면 if x ==4가 있어야함.
        #     break
        if arr[x]>arr[x+1]:
            arr[x], arr[x+1] = arr[x+1],arr[x]  #arr 두 공간을 서로 바꾸는 것

    if arr_save == arr:
        break
    arr_save = arr


print(arr)




#------------------------------------------------------
# 박지우 선생님 pick - bubble sort

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        pass


