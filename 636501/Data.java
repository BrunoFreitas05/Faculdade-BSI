public class Data implements MinhaData {
    private int dia;
    private int mes;
    private int ano;
    
    @Override
    public int getDia() {
        return dia;
    }

    @Override
    public int getMes() {
        return mes;
    }

    @Override
    public int getAno() {
        return ano;
    }

    @Override
    public void setDia(int dia) {
        if (dia > 0 && dia <= 31) {
            this.dia = dia;
        } else {
            throw new IllegalArgumentException("Dia inválido. Deve ser entre 1 e 31.");
        }
    }

    @Override
    public void setMes(int mes) {
        if (mes > 0 && mes <= 12) {
            this.mes = mes;
        } else {
            throw new IllegalArgumentException("Mês inválido. Deve ser entre 1 e 12.");
        }
    }

    @Override
    public void setAno(int ano) {
        this.ano = ano;
    }

    @Override
    public String mostrarData() {
        String[] meses = {"", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"};
        return dia + " de " + meses[mes] + " de " + ano;
    }
}
