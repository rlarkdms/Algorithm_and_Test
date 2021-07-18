# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 두개씩만 넣는거구나!!

#진짜 이상하게 풀었는데;;;

def solution(genres, plays):
    answer = []
    arr =[]
    dict={}#장르의 플레이 합
    dict_count={}# 2개씩 모을 때
    
    for i in range(len(genres)):#arr 리스트에 장르,plays수 고유번호 순으로 넣는다.
        arr.append([genres[i],plays[i],i])

    for j in range(len(genres)):
        if genres[j] in dict.keys():
            dict[genres[j]]=dict.get(genres[j])+plays[j]# 장르 플레이 합을 위한 것.
        else:
            dict[genres[j]]=plays[j]#일단 처음에는 dict에 추가하고 값 넣기.
            dict_count[genres[j]]=0#dict에 2개 씩 모으기위한 key넣기
    
    arr_sort=sorted(arr, key=lambda x: (x[1],-x[2]), reverse=True)#정렬 play수대로 그리고 고유번호 순으로
    new_dict=list(sorted(dict.items(), key=lambda x :x[1], reverse=True))#정렬 합의 수대로

    # 이거 sorted(dict.items())하고 그냥 dict, 하고 차이가 뭐지?
    # print(new_dict)
    # print(dict_count)
    for i in new_dict:
        for j in range(len(arr_sort)):
            if dict_count.get(i[0])>=2:#맞아 2를 넘어가면 break
                break
            if arr_sort[j][0]==i[0]:#만약 맞으면 
                dict_count[i[0]]=dict_count.get(i[0])+1#1 더하고
                answer.append(arr_sort[j][2])# answer에 append
 

    return answer