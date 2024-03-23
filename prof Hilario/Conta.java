class Conta{
    String numero;
    double saldo;
    public Conta(String nro,double saldoinicial){
        numero=nro;
        saldo=saldoinicial;
        
    }
    void credito(double valor){saldo = saldo +valor;}
    void debito(double valor){saldo=saldo-valor;}
}

class CriaConta{//arquivo cria conta.java
//criando um objeto do tipo conta
    public static void main (String[]args){
        Conta conta1 = new Conta("21.342-7",0); //criando um objeto
        conta1.credito(500.87);//referencia a metodos
        conta1.debito(45.00);
        System.out.println(conta1.saldo);

    }



}





