def solution(numbers, hand):
    answer = ''
    right=11
    left=10
    #사실 이 문제는 다 정해주면 금방 푸는 문제라 대가리 쓰지말고 다 정의해주기ㅋㅋㅋㅋㅋㅋㅋ
    
    for i in numbers:
        left_num=0
        right_num=0
        if i==1 or i==4 or i ==7:
            left=i
            answer+="L"
        elif i==3 or i==6 or i==9:
            right=i
            answer+="R"
        elif i==2:
            if left==1 or left==3 or left==5:
                left_num=1
            elif left==4 or left==8 or left==6:
                left_num=2
            elif left==7 or left==0 or left==9:
                left_num=3
            elif left==2:
                left_num=0
            else:
                left_num=4
                
            if right==1 or right==3 or right==5:
                right_num=1
            elif right==4 or right==8 or right==6:
                right_num=2
            elif right==7 or right==0 or right==9:
                right_num=3
            elif right==2:
                right_num=0
            else:
                right_num=4
        
            if right_num<left_num:
                answer+="R"
                right=2
            elif right_num>left_num:
                answer+="L"
                left=2
            else:
                if hand=='right':
                    answer+="R"
                    right=2
                if hand=='left':
                    answer+="L"
                    left=2

        elif i==5:
            if left==2 or left==4 or left==6 or left==8:
                left_num=1
            elif left==1 or left==3 or left==7 or left==9 or left==0:
                left_num=2
            elif left==5:
                left_num=0
            else:
                left_num=3
                
            if right==2 or right==4 or right==6 or right==8:
                right_num=1
            elif right==1 or right==3 or right==7 or right==9 or right==0:
                right_num=2
            elif right==5:
                right_num=0
            else:
                right_num=3
        
            if right_num<left_num:
                answer+="R"
                right=5
            elif right_num>left_num:
                answer+="L"
                left=5
            else:
                if hand=='right':
                    answer+="R"
                    right=5
                if hand=='left':
                    answer+="L"
                    left=5

        elif i==8:
            if left==5 or left==7 or left==9 or left==0:
                left_num=1
            elif left==10 or left==11 or left==4 or left==6 or left==2:
                left_num=2
            elif left==8:
                left_num=0
            else:
                left_num=3
                
            if right==5 or right==7 or right==9 or right==0:
                right_num=1
            elif right==10 or right==11 or right==4 or right==6 or right==2:
                right_num=2
            elif right==8:
                right_num=0
            else:
                right_num=3
        
            if right_num<left_num:
                answer+="R"
                right=8
            elif right_num>left_num:
                answer+="L"
                left=8
            else:
                if hand=='right':
                    answer+="R"
                    right=8
                if hand=='left':
                    answer+="L"
                    left=8

        elif i==0:
            if left==8 or left==10 or left==11:
                left_num=1
            elif left==5 or left==7 or left==9:
                left_num=2
            elif left==2 or left==4 or left==6:
                left_num=3
            elif left==0:
                left_num=0
            else:
                left_num=4
                
            if right==8 or right==10 or right==11:
                right_num=1
            elif right==5 or right==7 or right==9:
                right_num=2
            elif right==2 or right==4 or right==6:
                right_num=3
            elif right==0:
                right_num=0
            else:
                right_num=4
        
            if right_num<left_num:
                answer+="R"
                right=0
            elif right_num>left_num:
                answer+="L"
                left=0
            else:
                if hand=='right':
                    answer+="R"
                    right=0
                if hand=='left':
                    answer+="L"
                    left=0

            
    return answer