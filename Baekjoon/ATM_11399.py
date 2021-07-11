#인하 은행은 ATM기기가 1개 밖에 없음
#N명이 줄을 서있다.
# 1 / 1+2 / 1+2+3 / 1+2+3+3 / 1+2+3+3+4
# 1+3+6+9+13=32

n=int(input())
line_ATM_stand=list(map(int,input().split()))

line_ATM_stand.sort()

line_wait=[0]*n

line_wait[0]=line_ATM_stand[0]

for index in range(1,n):
    line_wait[index]=line_wait[index-1]+line_ATM_stand[index]

print(sum(line_wait))
