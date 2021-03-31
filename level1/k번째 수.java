import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        int[]array2;
        array2=new int[array.length];
        answer=new int[commands.length];//와 이거 선언때문에 엄청 오래걸렸네...
        
        
        for(int j=0; j<array.length; j++)
        {
            array2[j]=array[j];
        }//미리 저장 시켜둠. 

        for(int i=0; i < commands.length; i++){//열 개수만큼 돌림.           
                Arrays.sort(array,commands[i][0]-1,commands[i][1]);//짤라서 sorting 하고 //이건 확실히 맞아
               answer[i]=array[commands[i][0]+commands[i][2]-2];//i+k-2   
        
       for(int j=0; j<array.length; j++)
        {
            array[j]=array2[j];
        }        //다시 default로 저장
                
            }
        
        return answer;
    }
}