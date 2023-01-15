import sys
sys.stdin = open("input.txt", "rt")

works = list(map(int, input().split()))
n = int(input())
answer=0
while n > 0:
    n = n - 1
    works.sort(reverse=True)
    if works[0] == 0:
        break
    else:
        works[0] = works[0] - 1

for x in works:
    answer += x * x
print(answer)
print(works)

# 2차원 리스트로 한 풀이(정렬 X)
# 근데 max함수 시간복잡도도 O(n)..
# heap을 써서 풀어야함.
'''
arr = [[val, pos] for pos, val in enumerate(works)]
    #list(arr)
    tmp = max(arr) ## max value가 있는 value, index 를 뱉음
    #tmp[1] = max vaule가 있는 index
    #print(arr)

    #arr의 index에 접근해서 value를 깎아야함.
    # arr max val이 들어있는 index = arr[val][pos]
    # arr[tmp[1]][0]
    #print(type(arr))
    #print(type(arr[tmp[1]][0]))
    #arr[tmp[1]][0]-=1
    #print(arr[tmp[1]][0])
    #print(tmp)
    #print(arr)
    while n > 0:
        n = n - 1
        tmp=max(arr)
        if arr[tmp[1]][0] == 0:
            break
        else:
            arr[tmp[1]][0]-=1

    for i in range(len(arr)):
        answer+=arr[i][0]**2
        print(arr[i][0])
'''