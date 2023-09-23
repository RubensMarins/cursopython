from tkinter import *

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#configurando a janela
janela = Tk()
janela.title("")
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#criando labels......
label_app = Label(janela, text="Cronometro",fon=("Arial 10"), bg=cor1,fg=cor2)
label_app.place(x=8,y=5)

label_tempo = Label(janela, text="00:00:00", fon=("Times 50 bold"), bg=cor1, fg=cor4)
label_tempo.place(x=20,y=25)

#criando Botões............
botao_iniciar = Button(janela,text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_iniciar.place(x=20,y=130)

botao_pausar = Button(janela,text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_pausar.place(x=105,y=130)

botao_reiniciar = Button(janela,text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief="raised", overrelief="ridge")
botao_reiniciar.place(x=190,y=130)

janela.mainloop()
