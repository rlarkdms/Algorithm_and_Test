class Solution {
    public String solution(int a, int b) {
        String answer = "";
        int count=0;
    int Mouth[]={31,29,31,30,31,30,31,31,30,31,30,31};//이건 처음에 선언안되어있으면 풀기 
//어려운 문제라 생각해서 선언해둠. 
    String days[];
    days= new String[366];//윤년이니까 366일
        
        for(int i=0; i<days.length; i++){
         
            switch(i%7){     //i을 나눠서 일주일 돌아갈 때마다 요일 string 주기
                case 0:
                    days[i]="FRI";
                    break;
                case 1:
                    days[i]="SAT";
                    break;
                case 2:
                    days[i]="SUN";
                    break;
                case 3:
                    days[i]="MON";
                    break;
                case 4:
                    days[i]="TUE";
                    break;
                case 5:
                    days[i]="WED";
                    break;
                case 6:
                    days[i]="THU";
                    break;
            
            }
        }
        for(int j=0; j<(a-1); j++){//a월전 까지 다 더한다음에
        count=count+Mouth[j];
        }
        count=count+b-1;//b일도 더하고 -1->0부터 시작한게 아니라 1부터 시작해서
        
        answer=days[count];
       
            return answer;
    
    }
    
}