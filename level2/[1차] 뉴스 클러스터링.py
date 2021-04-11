def solution(str1, str2):
    str1_arr=[]
    str2_arr=[]
    str_gu_num_arr=[]
    str_wls_num_arr=[]
    str_hap_num_arr=[]
    str_num_arr=[]
    val=0
    count=0
    for i in range(0,len(str1)-1):#여기는 특수문자와 숫자빼고 다 소문자로 넣는 부분.
        if str1[i:i+2].isalpha():
            str1_arr.append(str1[i:i+2].lower())
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_arr.append(str2[i:i+2].lower())

    str_wls_num_arr=str1_arr+str2_arr#두개의 집합을 더한 찐 합집합.        
                
    for i in range(len(str1_arr)):#교집합 
        for j in range(len(str2_arr)):
            if str1_arr[i]==str2_arr[j]:
                str_gu_num_arr.append(str1_arr[i])
                str1_arr[i]=99
                str2_arr[j]=98
    
    str_gu_num_arr_copy=str_gu_num_arr.copy() 
    
    for i in range(len(str_wls_num_arr)):#찐 합집합에서 교집합을 뺀 찐 교집합 너무 야매인데;; 
        for j in range(len(str_gu_num_arr)):
            if str_wls_num_arr[i]==str_gu_num_arr[j]:

                str_gu_num_arr[j]=98
                str_wls_num_arr[i]=99
                break
    for k in str_wls_num_arr:
        if k!=99:
            str_hap_num_arr.append(k)
    
    if len(str_gu_num_arr_copy)==0 and len(str_hap_num_arr)==0:#만약 공집합이면
        val=1#1를 return
    else:
        val=len(str_gu_num_arr_copy)/len(str_hap_num_arr)# 공집합이 아니면 계산
        
    return int(65536*val)