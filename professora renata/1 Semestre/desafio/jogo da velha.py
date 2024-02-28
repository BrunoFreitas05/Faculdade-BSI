from tkinter import *

janela= Tk()
janela.title('Jogo Da Velha')
jogada=0

def X():
    img_botao=PhotoImage(file="imgX.png")

def O():
    img_botao=PhotoImage(file="imgO.png")

img_canvas= PhotoImage(file="jogo-da-velha.png")
canvasHud = Canvas(janela,bg='black', highlightthickness=0, width=800,height=800)
canvasHud.create_image(0, 0, image=img_canvas, anchor='nw')
canvasHud.place(rely=0.5,relx=0.5, anchor='center')

botao11=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao11.place(relx=0.25, rely=0.050)

botao12=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao12.place(relx=0.5, rely=0.190,anchor="center")

botao13=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao13.place(relx=0.675, rely=0.190,anchor="center")
#
botao14=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao14.place(relx=0.325, rely=0.5,anchor="center")
#
botao15=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao15.place(relx=0.5, rely=0.5,anchor="center")
#
botao16=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao16.place(relx=0.675, rely=0.5,anchor='center')
#
botao17=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao17.place(relx=0.325, rely=0.820,anchor="center")
#
botao18=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao18.place(relx=0.5, rely=0.820,anchor="center")
#
botao19=Button(janela,width=31,height=15,bg="black",border=0,activebackground="red",cursor="hand2")
botao19.place(relx=0.675, rely=0.820,anchor="center")





janela.config(bg='black')
janela.attributes('-fullscreen', True)
janela.mainloop()






