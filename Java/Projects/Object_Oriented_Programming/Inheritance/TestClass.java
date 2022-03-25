
public class TestClass {
    
    public static void main(String[] args) {

        Real_Number number = new Complex_Number(0.2,3);
        System.out.println(number.get_real());// Can not access the members of the subclass Complex_Number
        

        Complex_Number number2 = new Complex_Number(21,0.6);
        System.out.println(number2.get_real());
        System.out.println(number2.get_imaginary());

        
        
        
    }

    public void test_real_protected_method()
    {
       Real_Number real = new Real_Number(2);
        
    }
}
