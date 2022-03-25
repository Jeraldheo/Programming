import jeyson.projects.games.Create_Package;
import java.util.Scanner;

public class Test
{
    public static void main(String[]args)
    {
        Scanner input = new Scanner(System.in);
        String message = input.nextLine();
        Create_Package test = new Create_Package();
        test.print(message);
    }
}