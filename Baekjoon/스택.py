import sys
N=int(input())
arr=[[] for i in range(N)]

arr = [sys.stdin.readline() for i in range(N)]

stack=[]

for i in arr:
    if i[0:2]=='pu':
        stack.append(i[5:len(i)-1])
    elif i[0:2]=='to':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif i[0:2]=='si':
        print(len(stack))
    elif i[0:2]=='po':
        if len(stack)==0:
            print(-1)
        else:
            a=stack.pop()
            print(a)

    elif i[0:2]=='em':
        if len(stack)==0:
            print(1)
        else:
            print(0)


