import sys
sys.stdin=open("input.txt", "rt")
arr = []
ans=[]
for i in range(20):
    arr.append(i+1)
for i in range(10):
    n, m = map(int, input().split())
    #ans = arr[n-1:m]# = arr[n-1:m+1:-1]
    #print(ans)
    #ans = list(reversed(arr[n-1:m]))
    #print(ans)
    arr[n-1:m] = list(reversed(arr[n-1:m]))
for i in range(20):
    print(arr[i], end=" ")

'''
#강사풀이
a = list(range(21)) # 0~20까지 대입됨 그래서 마지막에 0번 인덱스를 pop해줘야 함
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e+i] = a[e+i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=" ")
'''
