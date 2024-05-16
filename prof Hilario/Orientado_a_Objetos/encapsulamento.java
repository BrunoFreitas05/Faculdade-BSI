package Orientado_a_Objetos;

public class encapsulamento {
    private String nro;
    private double saldo;
    public encapsulamento(String nro, double saldo){
        this.nro=nro;
        this.saldo=saldo;
    }
    //definicao dos metodos para manipular o saldo:
    //depositar, sacar e getSaldo.
    public void depositar(double valor){
        this.saldo+=valor;
    }
    public void sacar(double valor){
        this.saldo-=valor;
    }
    public double getSaldo(){
        return this.saldo;
    }






    }

    

