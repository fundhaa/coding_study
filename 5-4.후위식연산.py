import sys
sys.stdin = open("input.txt" ,"rt")

n = input()
stack = []
a=0
b=0
for x in n:
    if x.isdecimal() == 1:
        stack.append(x)
    else:
        if x=="+":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b+a)
        elif x=="-":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b-a)
        elif x=="*":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b*a)
        elif x=="/":
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b/a)
print(stack[0])