public class Carro {
    // Atributos
    private String marca;
    private String modelo;
    private int ano;
    private float velocidade;
 
    // Construtor
    public Carro(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.velocidade = 0;
    }
 
    // Método para acelerar o carro
    public void acelerar(int incremento) {
        this.velocidade += incremento;
    }
 
    // Método para frear o carro
    public void frear(int decremento) {
        this.velocidade -= decremento;
    }
 
    // Método para imprimir as informações do carro
    public void imprimirInformacoes() {
        System.out.println("Marca: " + this.marca + ", Modelo: " + this.modelo + ", Ano: " + this.ano + ", Velocidade: " + this.velocidade + " km/h");
    }
 
    // Método main para teste
    public static void main(String[] args) {
        // Criando um objeto carro
        Carro meuCarro = new Carro("Toyota", "Corolla", 2020);
 
        // Imprimindo informações do carro
        meuCarro.imprimirInformacoes();
 
        // Acelerando o carro
        meuCarro.acelerar(50);
        meuCarro.imprimirInformacoes();
 
        // Freando o carro
        meuCarro.frear(20);
        meuCarro.imprimirInformacoes();
    }
}
 