def solution(record):
    answer = []
    d={}
    enter=[]
    
    for i in record:#돌려 돌려 돌림판
        str=i.split()#문자열을 나누고
        if str[0]=='Enter':#각 케이스 별로 나누기#
            d[str[1]]=str[2]#엔터는 딕셔너리에 각각의 아이디와 이름 저장. 
            line=[]#이부분은 들어왔는지 나갔는지 아이디와 이름 매핑하는 부분.
            line.append("in")
            line.append(str[1])
            enter.append(line)
        elif str[0]=='Leave':#리브는 나갔는지 아이디와 이름 매핑하는 부분.
            line=[]
            line.append("out")
            line.append(str[1])
            enter.append(line)
        elif str[0]=='Change':#체인지는 말그대로 아이디를 키로 이름을 바꾸는 곳.
            d[str[1]]=str[2]
        

    for k in enter:#딕셔너리와 배열 매핑해서 넣어놓기. ex) 딕셔너리에서{"uid2934":"Muiz",....} [[in],[uid2934]]-> Muiz가 들어왔습니다. 
        sentence=""
        if k[0]=='in':
            sentence=sentence+d.get(k[1])+"님이 들어왔습니다." 
        else:
            sentence=sentence+d.get(k[1])+"님이 나갔습니다." 
        answer.append(sentence)
    
    return answer