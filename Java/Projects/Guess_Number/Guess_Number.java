import java.util.Random;
import java.util.Scanner;

public class Guess_Number
{
    public static void main(String[] args) {
        
        Integer CHANCES = 10;
        Random generator = new Random();
        Integer number = generator.nextInt(100) + 1;

        Scanner read = new Scanner(System.in);

        Integer guess = read.nextInt();
        System.out.println("Guesses left " + CHANCES);
        while(guess!=number && CHANCES>1)
        {   
            if(guess>number)
            {
                System.out.println("Left");
            }
            else
            {
                System.out.println("Right");
            }
            CHANCES--;
            System.out.println("Guesses left " + CHANCES);
            guess = read.nextInt();

        }

        read.close();
        
        if(guess==number)
        {
            System.out.println("Well done" + guess);
        }
        else
        {
            System.out.println("Game Over");
        }


    }
}