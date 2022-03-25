import java.util.Deque;
import java.util.ArrayDeque;
public class Solution
{
    public static void main(String[] args) {

        Deque bookStack = new ArrayDeque<String>();
        bookStack.push("Algorithms");
        bookStack.push("Number Theory");

        System.out.println(bookStack.peek());
        bookStack.pop();
        System.out.println(bookStack.peek());


        
    }
}