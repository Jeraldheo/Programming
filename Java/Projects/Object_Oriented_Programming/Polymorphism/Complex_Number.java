
public class Complex_Number extends Real_Number{

    private double imaginary;

    Complex_Number(double real, double imaginary)
    {
        super(real);
        this.imaginary = imaginary;
    }

    public void set_imaginary(double imaginary)
    {
        this.imaginary = imaginary;
    }

    public double get_imaginary()
    {
        
        return imaginary;
    }
    @Override
    public void type_number()
    {
        System.out.println("I am a complex number");
    }

    @Override
    public void print()
    {
        System.out.println("Testing Interface complex");
    }

 
}
