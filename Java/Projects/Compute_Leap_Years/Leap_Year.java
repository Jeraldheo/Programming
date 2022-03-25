

class Leap_Yea
{
    public static boolean is_leap_year(int year)
    {
        if(year%4==0)
        {
            if(year%100==0 && year%400!=0)
            {
                return false;
            }
            return true;
        }
        return false;
    }
    public static void main(String[]args) 
    {

        for(int i = 1600 ; i<=2100; i++)
        {
            if(is_leap_year(i))
            {
                System.out.println(i);
            }
        }
    
    }
}
