import java.util.Scanner;
public class Midia 
{
    private int codigo;
    private double preco;
    private String name;
    //Metodos para inserir valores nos campos.
    public void setCodigo(int codigo)
    {
        this.codigo = codigo;
    }
    public void setPreco(double preco) 
    {
        this.preco = preco;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    //Metodos para retornar os valores contidos nos campos.
    public int getCodigo()
    {
        return codigo;
    }
    public String getName()
    {
        return name;

    }
    public double getPreco()
    {
        return preco;
    }
    //Construtor sem paramentos.
    public Midia()
    {
        this(0,0.0,"Nenhum");
    }
    //Construtor  com paramentros.
    public Midia(int codigo, double preco, String name)
    {
        setCodigo(codigo);
        setPreco(preco);
        setName(name);
    }
    //Funcao para impressao dos dados do tipo.
    public String getTipo()
    {
        return "Midia: ";
    }
    //Funcao que retorna o conteudo dos campos em forma de String.
    public String getDetalhes()
    {
        return "Codigo: " + getCodigo() + "\n" +
                "Preco: " + getPreco() + "\n" +
                "Name: "  +  getName() + "\n";
    }
    //Funcao para impressao dos dados via getDetalhes()
    public void printDados()
    {
        String s = getTipo() + "\n" + getDetalhes() + "\n";
        System.out.println(s);
    }
    //Funcao para leitura dos dados via teclado
    public void inserirDados()
    {
        Scanner in = new Scanner(System.in);
        //Leitura dos dados do teclado
        System.out.printf("\n Entre com o codigo: ");
        int cod = in.nextInt();
        System.out.printf("\n Entre com o preco");
        double pre = in.nextDouble();
        in.nextLine(); //leitura do enter.
        System.out.printf("|n Entre com o nome: ");
        String nam = in.nextLine();
        //enviando os dados lidos para as funcoes set.
        setCodigo(cod);
        setPreco(pre);
        setName(nam);
    }
    }







