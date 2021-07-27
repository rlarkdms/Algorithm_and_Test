import sys

sys.setrecursionlimit(10000)

N=int(input())

arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

global zero_value

zero_value=0
global one_value

one_value=0

def t_or_f(arr,x_first,y_first,x_last,y_last):
    global one_value
    global zero_value
    standard=arr[x_first][y_first]
    for i in range(x_first,x_last):
        for j in range(y_first,y_last):
            if standard!=arr[i][j]:#만약 하나라도 다르면 4개로 짜르고 돌리고
                t_or_f(arr, x_first, y_first, (x_last-((x_last-x_first)//2)), (y_last-((y_last-y_first)//2)))#2사분면
                t_or_f(arr, (x_first+((x_last-x_first)//2)), y_first, x_last, (y_last-((y_last-y_first)//2)))#1사분면#아 바보였다...!
                t_or_f(arr, x_first, (y_first+((y_last-y_first)//2)), (x_last-((x_last-x_first)//2)), y_last )#3사분면
                t_or_f(arr, (x_first+((x_last-x_first)//2)), (y_first+((y_last-y_first)//2)), x_last,  y_last)#4사분면
#이 문제 오래걸렸는데 내가 이 범위를 착각해서 계속 메모리 오버가 났었다...ㅠㅠㅠ 바보같은게 범위를 잘못선택해서 같은 부분을 계속 돌고 있었다ㅠ...
                return 0
    #그 배열 안을 다 돌고 나왔을 때 만약 다 같은 숫자일 때->정사각형이 다 같은 숫자라는 뜻

    if standard==1:#숫자에 맞는 전역변수에 넣기
        one_value+=1
    else:
        zero_value+=1

    return 1
#반으로 가르고 반으로 가르고 반으로 가르고..

t_or_f(arr,0,0,len(arr),len(arr))
print(zero_value)
print(one_value)
