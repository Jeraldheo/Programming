import jeyson.projects.games.First_Package;
public class Using_Enum
{
    public enum Days{Monday, Tuesday, Wendsday, Thursday, Friday, Saturday, Sunday
    }

    public static void main(String[] args) {

        for(Days days: Days.values())
        {
            System.out.println(days);
        }
        
    }
}