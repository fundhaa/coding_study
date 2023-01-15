import sys
sys.stdin = open("input.txt", "rt")

m = input()

stack = []
res = ''
for x in m:
    if x.isdecimal():
        res+=x
    else:
        if x=="(":
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                res+=stack.pop()
            stack.append(x)
        elif x=="+" or x=="-":
            while stack and stack[-1]!="(":
                res+= stack.pop()
            stack.append(x)
        elif x==")":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.pop()

while stack: ## len(Stack)==0 일때까지 돌아감.
    res+=stack.pop()
print(res)
