import java.util.PriorityQueue;
import java.util.Scanner;
public class Solution
{

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        PriorityQueue p_queue = new PriorityQueue<Integer>();

        int num_entries = input.nextInt();

        for(int i = 0; i<num_entries; i++)
        {
            p_queue.add(input.nextInt());
        }

        System.out.println();

        while(!p_queue.isEmpty())
        {
            System.out.print(p_queue.poll() + " ");
        }

    }

}