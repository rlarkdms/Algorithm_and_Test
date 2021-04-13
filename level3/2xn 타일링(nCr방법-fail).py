# import math
# import operator as op
# from functools import reduce
# def solution(n):
#     answer = 0
#     standard=n
#     count=int(n/2)+1
#     for i in range(0,count):
#         answer+=ncr(standard,i)
#         standard-=1
#         answer=answer%1000000007
    
#     return answer
# def ncr(n,r):
#     if n<1 or r<0 or n<r:
#         raise ValueError
#     r=min(r,n-r)
#     numerator=reduce(op.mul, range(n,n-r,-1),1)
#     demominator=reduce(op.mul, range(1,r+1),1)
#     return numerator//demominator
# def conbin(n,r):
#     up=1
#     down=1
#     if r>int(n/2):
#         r=n-r
#     if r==0:
#         return 1
#     if r==1:
#         return n
#     for i in range(1,r+1):
#         down*=i
#         up*=n
#         n-=1

#     return round(up/down)

#시간 초과와 run타임 에러 등등 총체적 난국이 있어서 패턴을 분석해서 풀기로 함.
