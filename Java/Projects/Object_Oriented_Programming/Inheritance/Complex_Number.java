
public class Complex_Number extends Real_Number{

    private double imaginary;

    Complex_Number(double real, double imaginary)
    {
        super(real);
        this.imaginary = imaginary;
        binary_representation();
    }

    public void set_imaginary(double imaginary)
    {
        this.imaginary = imaginary;
    }

    public double get_imaginary()
    {
        
        return imaginary;
    }
}
