import java.util.Scanner;
public class TestGradeBook {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        
        String instructor = input.nextLine();
        String curse = input.nextLine();

        GradeBook gradeBook = new GradeBook(instructor, curse);
        gradeBook.display_Message();
    }
    
}
