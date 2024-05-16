import java.util.Scanner;
public class DVD extends Midia
{
 private int nFaixas;
 //construtor sem parametros.
 public DVD()
 {
    this (0,0.0, "Nenhum",0); //chamada ao construtor com parametros.
 }  
 //construtor com parametros.
 public DVD(int codigo, double preco, String name, int nFaixas)
 {
    super(codigo, preco, name);
    //chamada construtor da classe midia.
    setFaixas (nFaixas);
 }
 //função para impressao do tipo.
 public String getTipo()
 {
    return "DVD: ";
 }
 //função que retorna o conteudo do campos deste classe e da classe midia(usando o super !).
 public String getDetalhes()
 {
    return super.getDetalhes() + "\n" +
    "numero de faixas: " + nFaixas + "\n";
 }
 public void setFaixas(int nFaix)
 {
    nFaixas = (nFaix > 0 ) ? nFaixas:0;
 }
 //função para leitura dos dados via teclado dos campos desta classe e dos campos da classe mdidia(usando o super !).
 public void inserirDados()
 {
    //leitura dos dados contidos nos campos pertencentes a classe midia.
    super.inserirDados();
    Scanner in = new Scanner(System.in);
    System.out.printf("\n Entre com o numero de faixas: ");
    int nFaix = in.nextInt();
    setFaixas(nFaix);
 }
 
}