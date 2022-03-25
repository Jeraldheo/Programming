import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Solution
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        List data = new ArrayList();

        int initial_size = input.nextInt();

        for(int i = 0; i<initial_size; i++)
        {
            data.add(input.nextInt());
        }

        int num_queries = input.nextInt();

        for(int i = 0; i<num_queries; i++)
        {
            String operation = input.next();
            if(operation.equals("Insert"))
            {
                int value = input.nextInt();
                int index = input.nextInt();
                data.add(value, index);
            }
            
            if(operation.equals("Delete"))
            {
                int index = input.nextInt();
                data.remove(index);
            }
        }

        int final_size = data.size();
        for(int i = 0 ; i<final_size; i++)
        {
            System.out.print(data.get(i) + " ");
        }



    }
}