public class Aula10_ex2 {
    public static void main(String[] args) {
        ControleRemoto controle = new ControleRemoto();
    
    controle.addCanal(); //Canal:5
    controle.exibeCanal();
    controle.addCanal(); //Canal:6
    controle.exibeCanal();
    controle.addCanal(); //Canal:9
    controle.exibecanal();

    controle.addVolume(); //Volume:1
    controle.exibevolume();
    controle.subVolume(); //Volume:0
    controle.exibevolume();
    controle.subVolume(); //Volume:0
    controle.exibevolume();

    controle.setCanal(499); //Canal:500
    controle.exibecanal();
    controle.addCanal(); //Canal:3
    controle.exibecanal();
    controle.addCanal(); //Canal:5
    controle.exibecanal();



    }
}
