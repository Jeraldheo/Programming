
class Solul
{
    public static void main(String[] args)
    {
        java.util.Scanner input = new java.util.Scanner(System.in);
        String name = input.nextLine();

        

        Print_Solution print = new Print_Solution();

        System.out.println(print.getClass().getName());
        print.print_data(name);
    }
}