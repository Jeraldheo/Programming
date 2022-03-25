import java.util.ArrayList;
import java.util.Scanner;

public class Negative_Subarray
{

    public static void main(String[] args) {
        
        
        Scanner input = new Scanner(System.in);
        int size = input.nextInt();
        int count_negative = 0;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int i = 0; i<size; i ++)
        {
            arr.add(input.nextInt());
            if(arr.get(i)<0)
            {
                
                count_negative = count_negative + 1;
            }
        }

        ArrayList<ArrayList<Integer>> sum_subarrays = new ArrayList<ArrayList<Integer>>();
        sum_subarrays.add(arr);

        

        for(int i = 1; i<size; i++)
        {
            ArrayList<Integer> temp = new ArrayList<Integer>();

            for(int j = 0; j<sum_subarrays.get(i-1).size()-1; j++)
            {
                int sum_array = sum_subarrays.get(i-1).get(j) + sum_subarrays.get(0).get(i + j);
                temp.add(sum_array);
                if(sum_array<0)
                {
                    count_negative = count_negative + 1;
                }

            }

            sum_subarrays.add(temp);
        }

        
        System.out.println(count_negative);
    
    }

}