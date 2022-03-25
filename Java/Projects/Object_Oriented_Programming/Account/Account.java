public class Account
{
    private double balance;

    public Account(double initialBalance)
    {
        if(initialBalance>0)
        {
            balance = initialBalance;
        }
    }

    public void credit(double amount)
    {
        if(amount > 0)
        {
            balance = balance + amount;
        }
        else
        {
            System.out.println("The amount of money to credit has to be positive");
        }
    }

    public double getBalance()
    {
        return balance;
    }

    public void debit(double amount)
    {
        if(amount > balance)
        {
            System.out.print("\n Debit amount exceeded account balance \n");
        }
        else
        {
            balance = balance - amount;
        }
    }
}