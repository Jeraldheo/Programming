import java.util.ArrayList;
import java.util.stream.IntStream;

public class Using_Stream
{
    public static void main(String[] args) {
        ArrayList<Integer> data = new ArrayList<>();
        data.add(1);
        data.add(2);
        data.add(3);
        data.add(4);
        Double average = data.stream().mapToInt(Integer::intValue).average().getAsDouble();
        System.out.print(average);
       
    }
}