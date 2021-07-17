def solution(s):
    answer = ""
    dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    setence=""
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            setence+=i
            for k in dict.keys():
                if k==setence:
                    answer+=str(dict[k])
                    setence=""
    return int(answer)