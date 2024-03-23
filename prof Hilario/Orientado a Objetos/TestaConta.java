package Orientado a Objetos;


public class TestaConta{
    public static void main(String[] args) {
        Conta conta=new Conta("1234",100);
        conta.nro="4321"; //é possivel acessar o tributo de forma direta
        conta.saldo=200;
        System.out.println("Nro da conta: R$" +conta.nro);
        System.out.println("Saldo atual:R$"conta.saldo);

    }
}

