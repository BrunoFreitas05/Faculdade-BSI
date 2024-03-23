package Orientado a Objetos;

public class conta1 {
    public String nro;
    double saldo;
    public Conta(String nro,double saldo){
        this.nro=nro;
        this.saldo=saldo;

    }
    public void atualizaSaldo(double novoSaldo){
        this.saldo=novoSaldo;
    }
}//conta
