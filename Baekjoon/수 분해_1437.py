n=int(input())# 입력

dp=[0]*1000001 # N이 입력받을 수 있는 숫자+1 만큼 선언

dp[1]=1 #예외적인 부분들은 미리 선언
dp[2]=2
dp[3]=3
dp[4]=4

for i in range(5,n+1):
    dp[i]=(dp[i-3]*3)%10007 #점화식 적용


print(dp[n])
