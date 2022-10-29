import java.util.HashMap;
import java.util.Map;
public class Contacts_Manager
{
    private Map<String, Integer> contacts;

    public Contacts_Manager()
    {
        contacts = new HashMap<String, Integer>();
    }

    public void add_Contact(Contact contact)
    {
        String name = contact.get_name();
        if(contacts.get(name)==null)
        {
            contacts.put(name,contact.get_phone_number());
        }
        else
        {
            contacts.replace(name, contact.get_phone_number());
        }
    }

    public Integer search_contact(String name)
    {
        if(contacts.get(name)==null)
        {
            return -1;

        }

        return contacts.get(name);
    }

}