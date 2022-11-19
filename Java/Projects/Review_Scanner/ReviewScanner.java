import java.util.Scanner;

public class ReviewScanner
{
    public static void main(String[] args) {
        Boolean repeat = false;
        Scanner readInput = new Scanner(System.in);
        Double distance = 0.0;
        do
        {
            try
            {
                System.out.println("Input value: ");
                distance = Double.valueOf(readInput.nextLine());
                repeat = false;
            }
            catch(Exception exception)
            {
                System.out.println("Try again");
                repeat = true;
            }
            
        }while(repeat);
    }
}