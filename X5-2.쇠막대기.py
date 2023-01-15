import sys
sys.stdin = open("input.txt", "rt")
m = input()
stack = []
cnt = 0
for i in range(len(m)):
    if m[i]=="(":
        stack.append(m[i])

    elif m[i]==")" and m[i-1]=="(":
        stack.pop()
        cnt+=len(stack)

    elif m[i]==")" and m[i-1]!="(":
        cnt+=1
        stack.pop()

print(cnt)