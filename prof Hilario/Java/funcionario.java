
public class funcionario {
    double salario;
    public void setSalario(double salario){
        this.salario=salario + 500;
        }
    }
class analista extends funcionario{
    @Override
    public  void setSalario(double salario) {
        this.salario = salario + 100;
    }
}