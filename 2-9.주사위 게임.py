import sys
sys.stdin=open("input.txt","rt")
n = int(input())
arr = []
for i in range(n):
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0]==dice[1] and dice[1]==dice[2]:
        arr.append(10000+dice[0]*1000)
        continue
    if dice[0]==dice[1] and dice[1]!=dice[2]:
        arr.append(1000+dice[0]*100)
        continue
    if dice[1]==dice[2] and dice[0]!=dice[1]:
        arr.append(1000+dice[1]*100)
        continue
    if dice[0] != dice[1] and dice[1] != dice[2]:
        arr.append(dice[2]*100)
print(max(arr))
'''
arr = 0으로 잡고
if money>arr:
    arr = money
이런식으로 하면 리스트 하나를 덜 쓸 수 잇다. 메모리 측면에서 훨씬 나을듯
'''