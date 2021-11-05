# 8.zip을 사용하는 반복문 예시
print(f'-'*20)
print(f'zip사용')
arr1 = [1,2,3]
arr2 = [10,20,30,40]

for z in zip(arr1, arr2):
    print(z) #arr1과 교차되는 부분만 나옴
print(f'-'*20)

#-------------------------------------------

print(f'i만 사용하여 (방법1)')
#i만써서
#for x in range(arr1):
for x in arr1:
    print(f'[{x}:{arr2[x]}]')


print(f'-'*20)
#-------------------------------------------
print(f'i만 사용하여 (방법2)')

small = min(len(arr1), len(arr2))  #최소값
for i in range(small):
    print(f'({arr1[i]},{arr2[i]})')



