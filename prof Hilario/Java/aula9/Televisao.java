
public class Televisao {
    int Volume;
    int Canal;
    public void setvolume(int volume){
        if((volume<1)|| (volume>100)){
            this.Volume=1;
        }
        else{
            this.Volume=volume;
        }
    }
    public int getvolume()
    {
        return this.Volume;
    }

    public void setcanal(int canal){
        if((canal<1) || (canal>50)){
            this.Canal=1;
        }
        else{
            this.Canal=canal;
        }
    }
    public int getcanal()
    {
        return this.Canal;

    }
    public void Televisao(){
        this.setcanal(0);
        this.setvolume(0);
    }
    public void Televisao(int canal, int volume)
    {
        setcanal(canal);
        setvolume(volume);
    }
    public void subVolume()
    {
        setvolume(getvolume()+1);
    }
    public void descevolume()
    {
        setvolume(getvolume()-1);
    }
    public void sobeCanal()
    {
        setcanal(getcanal()+1);
    }
    public void desceCanal()
    {
        setcanal(getcanal()-1);
    }

}

