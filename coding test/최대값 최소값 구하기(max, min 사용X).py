#10.최대값 혹은 최소값을 구하는 알고리즘 직접 구현하기(max, min함수 쓰지 않고)

#ex) [3, 6, 2, 7]
#직접만든것

arr = [3,6,2,7,1,2,3,4,5,100]
large = arr[0]
small = arr[0]

for x in arr:
    if small > x:
        small = x
    elif x> large:
        large = x

print(f'최소값: {small}')
print(f'최소값: {large}')


#------------------------------------------
#값의 범위: 0~10 양끝 모두 포함
#arr1의 길이


#배운것
arr1 = [3,6,2,7]
result = arr[0]

#처음에 arr[0]과 arr[0]이 비교되므로 비효율적
for x in arr:
    #result: 기존값, x: 새로 들어오는 값
    if result<x:
        result = x


print(result)

