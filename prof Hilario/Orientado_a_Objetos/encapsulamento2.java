package Orientado_a_Objetos;

public class encapsulamento2{
    public static void main(String[] args) {
        encapsulamento2 conta=new encapsulamento2("1234",100);
        conta.saldo=200;
        conta.depositar(100);
        conta.sacar(50);
        System.out.println("Saldo atual:R$"+conta.getSaldo());
    }

}
