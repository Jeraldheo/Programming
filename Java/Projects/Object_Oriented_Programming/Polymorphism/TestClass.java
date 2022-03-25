
public class TestClass {
    
    public static void main(String[] args) {

        Real_Number number = new Real_Number(5);
        Real_Number number2 = new Complex_Number(6, 1);

        number.type_number();
        number2.type_number();

        Interface_Test inter = new Real_Number(2);
        Interface_Test inter2 = new Complex_Number(1, 2);

        inter.print();
        inter2.print();
        

        
        
        
    }

 
}
