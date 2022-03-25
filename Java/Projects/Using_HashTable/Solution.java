import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
public class Solution
{
    public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
        Map<String, Integer> phoneBook = new HashMap<String, Integer>();
		int n=in.nextInt();
		in.nextLine();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
            phoneBook.put(name, phone);
			in.nextLine();
		}
		while(in.hasNext())
		{
			String s=in.nextLine();
            Object phone = phoneBook.get(s);
            if(phone!=null)
            {
                System.out.println(s + "=" + phone);
            }
             
            if(phone == null)
            {
                System.out.println("Not Found");
            }
		}
	}
}