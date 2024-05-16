package Orientado_a_Objetos;

public class conta1 {
    public String nro;
    double saldo;
    public void Conta(String nro,double saldo){
        this.nro=nro;
        this.saldo=saldo;

    }
    public void atualizaSaldo(double novoSaldo){
        this.saldo=novoSaldo;
    }
}//conta
