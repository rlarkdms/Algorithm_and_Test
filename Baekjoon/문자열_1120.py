X,Y=input().split()

arr=[]
for i in range(len(Y)-len(X)+1):
    standard=0
    for j in range(len(X)):
        if Y[i+j]!=X[j]:#안맞는 부분을 1씩 더함. 이러면 이중 가장 Min을 고르면 됨.
            standard+=1
    else:
        arr.append(standard)

print(min(arr))