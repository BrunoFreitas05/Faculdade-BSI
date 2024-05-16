
public class Conta {
    private int numero;
    private double saldo;
    

    public int GetNumero(){
        return numero;
    }
    public double GetSaldo(){
        return saldo;
    }
    public void setNumero(int numero){
        this.numero = numero;
    }
    public void setSaldo(double saldo){
        this.saldo = saldo;
    }

    public void Creditar(double valor_creditado){
        this.saldo+=valor_creditado;
    }
    public void Debitar(double valor_debitado){
        this.saldo-=valor_debitado;
    }
    public void ExibirDadosConta(){
        System.out.println(this.numero);
        System.out.println(this.saldo);
    }

    public static void main(String[] args) {
        Conta Conta_1 = new Conta();
        Conta_1.setNumero(123456);
        Conta_1.setSaldo(500);
        Conta_1.Creditar(50);
        Conta_1.ExibirDadosConta();
        Conta_1.Debitar(100);
        Conta_1.ExibirDadosConta();

    }


}




