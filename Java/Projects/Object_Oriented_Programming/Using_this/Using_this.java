
public class Using_this
{
    private String message;

    public void set_message(String message)
    {
        this.message = message;

    }
    
    public void print_message(String message)
    {
        this.message = "I was not modified";
        System.out.println("Message given: "  + message);
        System.out.println("Message in the field: " + this.message);
    }

    public void print_message()
    {
        System.out.println(message);
    }


}