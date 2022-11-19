public class Main {

    public static void main(String[] args) {
        CheckingAccount checkingAccount = new CheckingAccount();
        SavingAccount savingAccount = new SavingAccount();
        CertificateOfDeposit certificateOfDeposit = new CertificateOfDeposit();
        

        checkingAccount.setBalance(100.0);
        System.out.println("Your checking account has balance: " + checkingAccount.getBalance());
    }
    
}
