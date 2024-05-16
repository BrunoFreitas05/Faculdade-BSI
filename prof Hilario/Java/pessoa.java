public class pessoa {
    private String nome;
    private String data_nasc;
    private double altura;
 
    public String getNome() {
        return nome;
    }
 
    public String getDataNasc() {
        return data_nasc;
    }
 
    public double getAltura() {
        return altura;
    }
 
    public void setNome(String nome) {
        this.nome = nome;
    }
 
    public void setdata_nasc(String data_nasc) {
        this.data_nasc = data_nasc;
    }
 
    public void setAltura(double altura) {
        this.altura = altura;
    }
    public void gettodos(){
        System.err.println(this.nome);
        System.err.println(this.altura);
        System.err.println(this.data_nasc);}
    public static void main(String[] args) {
        pessoa j2= new pessoa();
        j2.setNome("João");
        j2.setdata_nasc("10/05/1990");
        j2.setAltura(1.70);
        j2.gettodos();
 
     
    }
}
 