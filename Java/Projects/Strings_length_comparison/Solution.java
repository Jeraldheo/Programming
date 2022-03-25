import java.io.*;
import java.util.*;

public class Solution {
    
    public static String response(String A, String B)
    {
        if(A.equals(B))
        {
            return "No";    
        }
        
        int size_A = A.length();
        int size_B = B.length();
        
        int smaller_AB = Math.min(size_A, size_B);
        
        for(int i = 0; i<smaller_AB; i++)
        {
            char char_A = A.charAt(i);
            char char_B = B.charAt(i);
            if(char_A == char_B)
            {
                continue;
            }
            if(char_A > char_B)
            {
                return "Yes";
            }
            if(char_B > char_A)
            {
                return "No";
            }
            
        }
        
        if(size_A == smaller_AB)
        {
            return "Yes";
        }
        return "No";
    
    }

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        
        int size_A = A.length();
        int size_B = B.length();
        
        System.out.println(A.length() + B.length());
        System.out.println(response(A, B));
        
        String capitalized_A = Character.toUpperCase(A.charAt(0)) + A.substring(1);
        String capitalized_B = Character.toUpperCase(B.charAt(0)) + B.substring(1);
         
        System.out.println(capitalized_A + " " + capitalized_B);
        
        
    }
}



