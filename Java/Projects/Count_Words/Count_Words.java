import java.io.File;
import java.util.Scanner;

public class Count_Words
{
    public static void main(String[] args)throws Exception {
        File file = new File("data.txt");
        Scanner read_file = new Scanner(file);        
        int num_words = 0;
        do
        {
            String line = read_file.nextLine();
            num_words+= line.split(" ").length;
        }while(read_file.hasNextLine());

        System.out.println("Word Count: " + num_words);
    }

}