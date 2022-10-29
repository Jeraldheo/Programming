public class Contact {
    private String name;
    private Integer phone_number;

    public Contact(String name, Integer phone_number)
    {
        this.name = name;
        this.phone_number = phone_number;
    }

    public String get_name()
    {
        return name;
    }

    public Integer get_phone_number()
    {
        return phone_number;
    }
}
