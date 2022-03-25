import java.util.Scanner;

class Format_Output
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        String data = input.next();
        input.close();
        System.out.printf("%-15s%03d", data, data.length() );

    }
}