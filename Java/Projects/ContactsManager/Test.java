import java.util.Scanner;

public class Test {

    public static void main(String[] args) {
        Contacts_Manager myContacts_Manager = new Contacts_Manager();

        Contact friend = new Contact("Jeyson", 33883511);
        Contact friend2 = new Contact("Jerald", 33883512);
        Contact friend3 = new Contact("Marin", 33883513);
        Contact friend4 = new Contact("Norales", 33883514);

        myContacts_Manager.add_Contact(friend);   
        myContacts_Manager.add_Contact(friend2);
        myContacts_Manager.add_Contact(friend3);
        myContacts_Manager.add_Contact(friend4);

        System.out.println(myContacts_Manager.search_contact(friend.get_name()));
        System.out.println(myContacts_Manager.search_contact(friend2.get_name()));
        System.out.println(myContacts_Manager.search_contact(friend3.get_name()));
        System.out.println(myContacts_Manager.search_contact(friend4.get_name()));
        System.out.println(myContacts_Manager.search_contact("Juan"));

        System.out.println("Let's create our own contact");
        System.out.println("Give me the name");
        Scanner read = new Scanner(System.in);
        String name = read.nextLine();
        System.out.println("Give me the phone number");
        Integer phone_number = read.nextInt();

        Contact contact = new Contact(name, phone_number);
        myContacts_Manager.add_Contact(contact);
        
        read.nextLine();
        System.out.println("Enter the name contact you want to search for");
        String search_name = read.nextLine();
        
        System.out.print(myContacts_Manager.search_contact(search_name));
        

    }
    
}
