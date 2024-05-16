import javax.swing.JOptionPane;


public class CaixaDeDialogo {
    public static void main(String[] args) {
        String nome;
        int resposta;
        nome =JOptionPane.showInputDialog("Qual o seu nome ?");
        resposta = JOptionPane.showConfirmDialog(null,"Seu Nome?"+nome);
        if(resposta==JOptionPane.YES_OPTION){
            //Verifica se o usuario clicou no botao yes
            JOptionPane.showMessageDialog(null,"Nome Correto!");
        }
        else{
            JOptionPane.showMessageDialog(null,"Nome Incorreto!");
        }

    }
}