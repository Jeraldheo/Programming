
import java.util.stream.Stream;

public class PrintStream
{
    public static void main(String[] args) {
        String[] data = {"Hello", "World", "Good"};
        Stream.of(data).forEach(System.out::println);

    
        
    }
}