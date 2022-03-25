import java.util.ArrayList;
import java.util.Scanner;
public class Solution
{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<ArrayList<Integer>> data = new ArrayList<ArrayList<Integer>>();
        
        for(int i = 0; i<4; i++)
        {
            ArrayList<Integer> temp = new ArrayList<Integer>();
            for(int j = 0; j<4; j++)
            {

                temp.add(input.nextInt());
            }
            data.add(i,temp);
        }

        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                System.out.print((data.get(i)).get(j));;
            }
            System.out.println();
        }
    }
}