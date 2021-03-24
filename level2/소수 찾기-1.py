from itertools import permutations
def solution(numbers):
    answer = 0
    number=[]
    count=[]
    origin=[]
    prime_arr=[]
    for j in numbers:
        number.append(j)
    
    for i in range(1,len(numbers)+1):#숫자 갯수
        count.append(list(map(''.join,permutations(number,i))))
    
    for k in count:
        for j in k:
            origin.append(int(j))

    prime_arr=list(set(origin))
    prime_arr.sort()
    if 0 in prime_arr:
        prime_arr.pop(0)
    if 1 in prime_arr:
        prime_arr.pop(0)
        
    for i in prime_arr:
        for j in range(2,int(i/2+1)):
            if i%j==0:
                break                
        else:
            answer+=1
    
    return answer