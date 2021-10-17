#LIS 알고리즘이라고 함.

n=int(input())
arr=list(map(int,input().split()))

arr.reverse()
dp=[1]*n
max_value=arr[0]
answer=1
max_arr_value=0
#배열 값보다 하나 더 커야 함.
# for i in range(1,len(arr)):
#
#     # print("max_value:%d, arr[i]:%d, max_arr_value:%d" %(max_value,arr[i],max_arr_value))
#     # print(dp)
#
#     if max_value<=arr[i]:# 더 클때
#         dp[i] = dp[max_arr_value] + 1
#         max_value=arr[i]
#         max_arr_value=i

    #
    # elif max_value==arr[i]:# 더 작은 때
    #     dp[i]=dp[max_arr_value]
max_value=1
for i in range(n):
    dp[i]=1
    for j in range(i):#아 이게 지금 i가 1이라고 셋해놓고 맨 마지막꺼랑 비교해서 더 크고,아 그렇니까 i번째가몇번째로 큰건지 확인하는 과정
        if arr[j]<arr[i] and dp[j]+1>dp[i]: #아 더 큰게 나올때마다 갱신하는 거구나...그래서 진짜 큰게 나왔을 때 셋.
            dp[i]=dp[j]+1
            if max_value<dp[i]:#가장 큰 값으로 설정하거나 그냥 max(dp)해도 똑같음. dp에서 가장 큰 값==최장 수열임.
                max_value=dp[i]

#이해가 좀 안되는데??? ->LIS 알고리즘이 이해가 안돼서 인터넷 카피함.
#https://source-sc.tistory.com/14

print(n-max_value)
# standard=0
# sum_max=0
# for k in range(n):
#     standard=0
#     sum_value=0
#     for j in range(k,n):
#         if arr[j]>=standard:
#             standard=arr[j]
#             sum_value+=1
#     sum_max=max(sum_max,sum_value)
# print(n-sum_max)


