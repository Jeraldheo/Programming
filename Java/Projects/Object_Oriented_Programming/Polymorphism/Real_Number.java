
public class Real_Number implements Interface_Test
{
    private double real;
    

    Real_Number(double number)
    {
        real = number;
    }

    public void set_real(double number)
    {
        real = number;
        type_number();
    }
    public double get_real()
    {
        return real;
    }

    public void type_number()
    {
        System.out.println("I am a real number");
    }

    public void print()
    {
        System.out.println("Testing Interface real");
    }

 

}