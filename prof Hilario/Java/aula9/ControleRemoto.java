public class ControleRemoto {
    private Televisao televisao;
    public ControleRemoto ()
    {
        this.televisao = new Televisao();
    }
    public void addVolume ()
    {
        this.televisao.subVolume();
    }
    public void subVolume()
    {
        this.televisao.descevolume();
    }
    public void setVolume (int volume)
    {
        this.televisao.setvolume (volume);
    }

    public int getVolume()
{
    return this.televisao.getvolume();
}
public void exibevolume ()
{
    System.out.println("Volume: "+ getVolume());
}

public void addCanal()
{
    this.televisao.sobeCanal();
}

public void subCanal()
{
    this.televisao.desceCanal();
}

public void setcanal (int canal)

{
    this.televisao.setcanal (canal);
}


public int getcanal()

{
    return this.televisao.getcanal();
}

public void exibeCanal()

{
    System.out.println("Canal: "+ getCanal());
}

public void setCanal (int canal)

{
    this.televisao.setcanal (canal);
}


public int getCanal ()

{
    return this.televisao.getcanal();

}

public void exibecanal()

{
    System.out.println("Canal: "+ getCanal());

}



}

