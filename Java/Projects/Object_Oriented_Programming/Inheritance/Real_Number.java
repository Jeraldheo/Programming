
public class Real_Number
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

    private void type_number()
    {
        System.out.println("I am a real number");
    }

    protected void binary_representation()
    {
        System.out.println("Binary representation");

    }
}