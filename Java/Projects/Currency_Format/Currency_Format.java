import java.text.*;
import java.util.*;


class Currency_Format
{
    public static void main(String[] args)
    {
        System.out.println(NumberFormat.getCurrencyInstance().format(5));
        Locale  locale_india =  new Locale("en", "IN");
        System.out.println(NumberFormat.getCurrencyInstance(locale_india).format(5));

    }
}