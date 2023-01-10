import sys
sys.stdin=open("input.txt", "rt")
t = int(input())
for i in range(0, t):
    n, s, e, k = map(int, input().split())
    ans=list(map(int, input().split())) # 리스트형으로 입력을 저장하기
    ans = ans[s-1:e]
    ans.sort()
    print("#%d %d" %(i+1, ans[k-1]))
