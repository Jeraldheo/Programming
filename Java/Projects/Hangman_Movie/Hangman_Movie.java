import java.io.File;
import java.util.Scanner;

public class Hangman_Movie
{
    public static void main(String[] args) throws Exception{
        
        File movies = new File("movies.txt");
        Scanner read_movies = new Scanner(movies);
        Integer num_letters = 0;
        Integer num_spaces = 0;
        String movie = read_movies.nextLine();
        Integer num_characters = movie.length();
        for(int i = 0; i<num_characters;i++)
        {
            if(movie.indent(i)==" ")
            {
                num_spaces+=1;
            }
        }

        

    }
}