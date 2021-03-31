class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
     
 
        int having[];//체육복 있는 학생 없는 학생 표시하기 위한 배열 having
        //0은 체육복 있는것 
        //1은 체육복 없는것
        having =new int[n];//다 0으로 set
        for(int j=0; j<lost.length; j++){//2.lost랑 reserve 상쇄
            for(int z=0; z<reserve.length; z++){

                if(lost[j]==reserve[z]){
                     lost[j]=0;
                    reserve[z]=0;//
                }
            }
        }
        
        for(int i=0; i<lost.length; i++){
            if(lost[i]!=0)//이유가 앞에서 lost랑 reserve 상쇄함
                having[lost[i]-1]=1;//lost 배열값의 -1 값은 다 1로 set
        }   

        //이게 여기가 중요하네
        for(int k=0; k<reserve.length; k++){
            
         if(reserve[k]==1){//reserve의 배열값이 1이면 맨 앞에 학생이니 
												   //그 뒤에 학생에게 체육복 주기
                if(having[reserve[k]]==1){//체육복이 없으면
                     having[reserve[k]]=0;//뒤에 학생 체육복 주기
            
                }
         }
         else if(reserve[k]==n){//reserve의 배열값이 n이니 맨 뒤에 학생임.
             
                    if(having[reserve[k]-2]==1){//앞에 학생이 체육복이 없으면 
                    having[reserve[k]-2]=0;//체육복 주기
         
                    }
         
         }else if(reserve[k]!=0){

                if(having[reserve[k]-2]==1){//앞에 학생이 체육복 없으면
                    having[reserve[k]-2]=0;//체육복 주기
                }
                else if(having[reserve[k]]==1){//뒤에 학생이 체육복 없으면
                     having[reserve[k]]=0;//체육복 주기
                }   
            }
        }
        for(int s=0; s<having.length; s++){
            
            if(having[s]==0)//체육복 있는 사람 
            answer++;//숫자 세기
            
        }
        
          return answer;   
    }
}
//문제 먼저 이해하자
//1.lost배열은 체육복을 잃어버린 아이들임
//2.reserve는 여벌의 체육복이 있는 학생임
//3.근데 reserve랑 lost는 겹칠수 있고 그러면 reserve는 상쇄됨.
//4.체육복은 앞뒤 학생에게만 빌려줄 수 있음.->이럴경우 맨앞이랑 맨뒤 고려, 무조건 앞에 아이한테 우선권