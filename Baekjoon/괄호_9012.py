n=int(input())
#스택 문제
def cal(str):
    arr=[]
    for i in str:
        if i=='(':
            arr.append('(')
        else: # ')'일 때
            if not arr: #비었을 때
                return "NO"
                break
            else:
                arr.pop()
    else:
        if not arr: #비어있으면
            return "YES"
        else:
            return "NO"


for i in range(n):
    str=input()
    print(cal(str))