class Solution {

    public int solution(int[][] board, int[] moves) {
        int answer = 0;//인형 터트리는 개수      
        int count=0; //result 개수 세는 용도 
        int result[];//이게 저 크레인으로 옴긴 인형의 배열
        
        result =new int[1000];//move의 개수는 1000개까지 가능하다고 하니 1000개로 초기화!
        
        
    for(int i=0; i<moves.length; i++){//이게 move의 개수만큼 도는데

        for(int j=0; j<board[0].length; j++){//열의 개수만큼돌기

            if(board[j][moves[i]-1]!=0){//moves의 값의 [0][0] [1][0] [2][0] 이런식으로 값을 탐색함 
                // 0이 아닌 값을 찾으면 result에다 그 값을 넣음 
                result[count]=board[j][moves[i]-1];
        
                
                if((count>0)&&(result[count]==result[count-1])){
//이 부분이 터트리는 부분 count>0을 한 이유는 count 1이라는 조건을 안주면 에러남 
//들어오는 것중에 result[count]와 result[count-1]의 값이 같으면 펑펑!  
                    answer=answer+2;//그리고 인형 두개 깨짐
                    count--;//이건 ㅁㅁㅁㅁ|ㅁ  |부분에서 명령이 들어간거여서 한걸음 뒤로가야함.
                }
                else {

                    count++;//아니면 한발자국 나가고
                }
                
                board[j][moves[i]-1]=0;//인형 빠지면 0으로 채우고
              
                break;//이번 반복문은 패스!
            }
            
        }
    }   
        


        return answer;
    }
}