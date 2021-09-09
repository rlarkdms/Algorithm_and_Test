def solution(rows, columns, queries):
    answer = []
    arr=[]
    
    for i in range(rows):
        sentence=[]
        for j in range(1,columns+1):
            sentence.append((i*columns)+j)
        arr.append(sentence)
        
    # for i in queries:
    #     bingbing(querites)
    return answer
#아 문제 풀다가 저장안됐네...