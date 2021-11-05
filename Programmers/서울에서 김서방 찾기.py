# seoul = ["Jane", "Kim"]
# count = 0
# for x in range(0,len(seoul)):
#     if "Kim" == seoul[x]:
#         break
#     else:
#         count += 1
#
# answer = f'김서방은 {count}에 있다'
#
# print(answer)

seoul = ['Jane', 'Kim']
print('김서방은 {}에 있다'.format(seoul.index('Kim')))