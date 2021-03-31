def solution(n, m):
    answer = []
    comfirm=True
    for i in range(n,0,-1):
        if n%i==0:
            for j in range(m,0,-1):
                if m%j==0:#공약수를 뒤부터 접근해서
                    if i==j:#만약 같으면
                        comfirm=False
                        answer.append(i)#넣고
                        break
        if comfirm==False:#계속 도는 이유로 또 False은 break로 하고
            break
    
    k1=1    
    k2=1
      
    while k1*n!=k2*m:#둘이 값이 다를 동안만도는데 
        if k1*n<k2*m:#만약 한쪽이 크면 안 큰 쪽의 곱하기 개수를 업
            k1+=1
        if k1*n>k2*m:#똑같이 한쪽이 크면 안 큰쪽의 곱하기 개수를 업업!
            k2+=1
    answer.append(k1*n)        
    return answer