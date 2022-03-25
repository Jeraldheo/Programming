
public class AccountTest {

    public static void main(String[] args)
    {
        Account account1 = new Account(25);
        Account account2 = new Account(-3);

        System.out.printf("Acconts initial balance: \n%.2f\n%.2f\n", account1.getBalance(), account2.getBalance());

        account1.debit(25);

        System.out.printf("Acconts after debit to account1: \n%.2f\n%.2f\n", account1.getBalance(), account2.getBalance());

    }
    
}
