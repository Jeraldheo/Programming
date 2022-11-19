import java.util.Scanner;
import java.util.stream.Stream;

public class DistanceClosestBigger
{
    public static void main(String[] args) {
    
        Scanner readData = new Scanner(System.in);
        int[] data = Stream.of(readData.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int index = readData.nextInt();
        readData.close();

        int firtBiggerRight =  getFirstBiggerRight(index, data);
        int firtBiggerLeft =  getFirstBiggerLeft(index, data);

        int distanceRight = firtBiggerRight - index;
        int distanceLeft = index - firtBiggerLeft;

        int distance = Math.min(distanceLeft, distanceRight);
        if(distance == 0)
            distance = Math.max(distanceLeft,distanceRight);

        System.out.println("Distance closest bigger: " + distance);


    }

    private static int getFirstBiggerRight(int index, int[]data)
    {
        int length = data.length;
        for(int i = index + 1; i<length; i++)
        {
            if(data[index]<data[i])
            {
                return i;
            }
        }
        return index;
    }

    private static int getFirstBiggerLeft(int index, int[]data)
    {
        for(int i = index - 1; i>=0; i--)
        {
            if(data[index]<data[i])
            {
                return i;
            }
        }
        return index;
    }


}
