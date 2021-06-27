n,m=map(int,input().split())

arr=list(map(int,input().split()))

result=0
start=0
end=0
while(end<=n):
  sum_value=sum(arr[start:end])

  if sum_value==m:
    end+=1
    result+=1
  elif sum_value>m:
    start+=1
  elif sum_value<m:
    end+=1

print(result)