import java.util.Arrays;
import java.util.Scanner;

public class Solution
{
    public static void print(int[] arr)
    {
        for(int i = 0; i<arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
    }
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.println("Insert how many values you want to work with: ");

        int size = input.nextInt();
        int[] arr = new int[size];

        System.out.println(arr.length);
        System.out.println("Insert the values");

        for(int i = 0; i<size; i++)
        {
            arr[i] = input.nextInt();
        }

        System.out.println("This is the data you gave us");
        print(arr);

        System.out.println("This is the data sorted");
        Arrays.sort(arr);

        print(arr);

        System.out.println("Insert Value to search: ");
        int key = input.nextInt();
        System.out.println("The position of " + key + "is " + Arrays.binarySearch(arr, key));
    }
}