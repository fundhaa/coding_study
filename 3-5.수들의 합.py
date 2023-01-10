import sys
sys.stdin=open("input.txt", "rt")
n, m = map(int, input().split())
arr=list(map(int,input().split()))

cnt = 0
ans = 0
p1=0
p2=p1
while(p1<n):
    cnt+=arr[p2]
    if cnt==m:
        # 정답 발견 & 다음 단계
        ans+=1
        p1+=1
        p2=p1
        cnt=0
    elif cnt<m:
        # 현 단계
        p2+=1
        if p2>=n:
            break
    else:
        # 다음 단계
        p1+=1
        p2=p1
        cnt=0
    #if p1>=n-1:
    #    break

if arr[n-1]==m:
    ans+=1
    print(ans)
else:
    print(ans)