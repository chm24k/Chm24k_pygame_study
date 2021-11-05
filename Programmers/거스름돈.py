a = input('값을 입력하시오. >> ')
a = int(a)

list1 = [500,100,50,10]

count = 0

while (True):
    print(f'{list1[count]}원: {a//int(list1[count])}')
    a = a%list1[count]
    count+=1
    if count ==int(len(list1)):
        break