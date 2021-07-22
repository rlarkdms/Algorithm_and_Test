# 방금 그 곡
# 1) 방송국에서는 한 음악을 반복해서 재생할 때도 있어서 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디 일 수도 있다.
# 2) 반대로 중간에 노래가 끊길 수 있어서 네오가 생각한 노래가 아닐 수도 있다.
# 3) 음악제목,재생이 시작되고 끝난 시간,악보 제공.
# 4) 조건이 일치하는 곳이 여러개 일 경우 재생된 시간이 제일 긴 제목을 반환한다. 재생된 시간도 같을 경우는 먼저 입력된 음악의 제목을 반환.
# 5) 조건에 일치하는 곡이 없을 경우는 "None" 반환.

def solution(m, musicinfos):
    answer_arr=[]#조건에 일치하는 시간과 제목 넣는 리스트
    memory=[]#m의 문자열을 list화 하는 리스트(#같은거 처리하기 위해서 따로 리스트 선언)
    
    for i in range(len(m)):# '#'붙여서 리스트에 넣는 과정 
        if m[i]=='#':
            memory.pop()
            memory.append(m[i-1]+"#")#만약 #이면 그전꺼 pop하고 한꺼번에 넣기.
        else:
            memory.append(m[i])

    for i in range(len(musicinfos)):# 연산하기 위해 for 문을 돌기
        time=0#1분 단위로 알기위해서 time 변수 선언
        memory_list=[]#musicinfos의 멜로디를 알기 위해 memory_list 리스트 선언
        memory_music=[]#memory_list에 시간을 적용한 리스트 선언
        arr=musicinfos[i].split(',')# ','에 따라 나누기 arr[0]-> 시작 시간 arr[1]->끝나는 시간 arr[2]->"노래 제목", arr[3]->멜로디
        time=((int(arr[1][0:2])-int(arr[0][0:2]))*60)+(int(arr[1][3:5])-int(arr[0][3:5]))#분으로 시간 구하기
        
        for i in range(len(arr[3])):# 앞과 똑같이 멜로디에 #를 붙여서 memory_list에 넣는 과정. 
            if arr[3][i]=='#':
                memory_list.pop()
                memory_list.append(arr[3][i-1]+"#")
            else:
                memory_list.append(arr[3][i])
        
        for k in range(time//len(memory_list)):#memory_list에 시간을 적용하는 과정. 그 후 memory_music 리스트에 적용
            memory_music.extend(memory_list)
        memory_music.extend(memory_list[0:time%len(memory_list)])

        
        for k in range(len(memory_music)-len(memory)+1):#m의 리스트와 memory_music을 일일이 비교.
            if memory_music[k:k+len(memory)]==memory:#만약 조건에 부합하면 break
                answer_arr.append([time,arr[2]])
                break

                
    memory_sort=sorted(answer_arr, key=lambda x:x[0], reverse=True)#같은 조건이 있을시를 위해 시간으로 sorting

    if len(memory_sort)==0:#조건 만족 못할 때에는 None
        return "(None)"
    else:
        return memory_sort[0][1]#만족할 때는 sorting 된것 중에 맨 앞에 꺼.