import static java.lang.Math.pow;
public class Test_Aliens {
    
    public static void main(String[] args)
    {
        System.out.println("Number of aliens on planet Earth years ago " + Aliens.get_num_aliens());

        Aliens alien1 = new Aliens();
        Aliens alien2 = new Aliens();

        if(alien1.get_num_aliens() == alien2.get_num_aliens())
        {
            System.out.println("Number of aliens now " + alien1.get_num_aliens());
        }

        System.out.println("Square the number of aliens: " + pow(Aliens.get_num_aliens(), 2));
        
    }
}
