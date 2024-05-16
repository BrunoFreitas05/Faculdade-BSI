import java.util.Scanner;
public class CD  extends Midia
{
    private int nMusicas;
    //Construtor sem paramentros
    public CD()
    {
        //chmada ao construtor com parametro
        this(0,0.0,"Nenhum",0);
    }
    //Construtor com parametros
    public CD(int codigo, double preco, String name, int nMusicas)
    {
        //Chamada ao consgtrutor da classe Midia
        super(codigo,preco,name);
        setMusica(nMusicas);
    }
    //Funcao para impressao do tipo
    public String getTipo()
    {
        return "CD: ";
    }
    //Funcao que retorna o conteudo do campos desta classe e da classe Midia(usando Super)
    public String getDetalhes()
    {
        return super.getDetalhes() + "\n" +
                "Numero de musicas: " + nMusicas +"\n";
    }
    public void setMusica(int nmus)
    {
        nMusicas = (nmus > 0) ? nmus :0;
    }
    //Funcao para leitura dos dados via teclado dos campos desta classe e  dos campos da classe Midia (usando super)
    public void inserirDados()
    {
        //Leitura dos dados dos campos campos pertecentes a classe Midia.
        super.inserirDados();
        Scanner in = new Scanner(System.in);
        System.out.printf("\n Entre com o numero de musicas: ");
        int nmus = in.nextInt();
        setMusica(nmus);
    }





}
