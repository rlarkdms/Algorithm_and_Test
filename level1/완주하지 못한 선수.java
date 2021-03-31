import java.util.Arrays;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
 
        Arrays.sort(participant);//두배열을 다 오름차순으로 sort한다!!!
        Arrays.sort(completion);
  
        for(int i=0; i<completion.length; i++){
            if(!participant[i].equals(completion[i])){
             //만약 달라지는 부분 생기면 그 부분이 답이다!!!   
             answer=participant[i];   //그래서 answer에 넣고 
                break;//시간아까우니까 break~~
            }            
        } 
        if(answer.equals("")){//여기서 participant가 1 더큰데 만약 participant의 가장 마지막일 경우에는
            answer=participant[participant.length-1];//그게 답
        }
        return answer;  
    }
        
}