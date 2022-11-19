public class Main
{
    public static void main(String[] args) {
        String data = null;
        System.out.println(data);

        String data1 = "full";
        String data2 = "well";
        System.out.println(data1.compareTo(data2));//negative
        System.out.println(data2.compareTo(data1));//positive
        System.out.println(data1.compareTo("full"));//cero

    }
}