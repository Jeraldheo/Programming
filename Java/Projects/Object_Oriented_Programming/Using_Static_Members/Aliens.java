public class Aliens
{
    private static int num_aliens = 0;

    public Aliens()
    {
        num_aliens++;
    }

    public static int get_num_aliens()
    {
        return num_aliens;
    }
}