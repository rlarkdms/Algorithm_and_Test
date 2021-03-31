class Solution {
    public String solution(String s) {
        String answer = "";
        
        if(s.length()%2==0){
            //짝수            
            answer=s.substring((s.length())/2-1,(s.length())/2+1);
//짝수면 중간 두글자 가져오기
        }else{
            //홀수
            answer=s.substring((s.length())/2,(s.length())/2+1);
//홀수면 중간에 글자 가져오기
        }
        return answer;
    }
}