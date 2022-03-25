import java.util.Deque;
import java.util.ArrayDeque;

public class Solution
{
    public static boolean isBlanced(String data)
    {
        Deque stack = new ArrayDeque<Character>(); 
        char[] values  = data.toCharArray();
        

        for(char element : values)
        {
            if(element == '[' || element == '(' || element == '{')
            {
                stack.push(element);
            }
            else
            {
                if(stack.isEmpty())
                {
                    return false;
                }
                Character top = (Character)stack.pop();
                if((top.equals('[') && element!=']') || (top.equals('(') && element!=')') || (top.equals('{') && element!='}'))
                {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args)
    {
        System.out.println(isBlanced(""));
    }

}