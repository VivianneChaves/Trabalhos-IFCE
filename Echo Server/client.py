import socket, json
from tkinter import *

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
while True:
    def enviar():
        #Enviando as variáveis para o server
        vp = txt.get()
        n = txt1.get()
        client.sendall(bytes(vp, 'UTF-8'))
        client.sendall(bytes(n, 'UTF-8'))

        # Recebendo as variáveis do server
        data = client.recv(2048)
        data = json.loads(data.decode('ascii'))
        #Usei o round para mostar apenas duas casas decimais e depois passei para string novamente
        vf = round(float(data[0]),2)
        vparc = round(float(data[1]),2)
        je = round(float(data[2]),2)
        vf_aux = str(vf)
        vpar_aux = str(vparc)
        je_aux = str(je)
        lbl = Label(window, text="Valor final = " + vf_aux + "\nValor da parcela = " + vpar_aux + "\nJuros efetivo = " + je_aux, font="Times 15")
        lbl.grid(column=0, row=9,)

    def JanelaCreditos():
        newwindow = Toplevel(window)
        newwindow.title("Sobre")
        newwindow.maxsize("320", "180")
        lbl = Label(newwindow, text = "Esse projeto foi feito durante a cadeira de\n Sistemas Operacionais de Redes I, com auxílio do \n professor José Roberto", font = "Times 12", justify  = LEFT)
        lbl.grid(column = 0, row = 0)
        lbl = Label(newwindow, text= "===X==CRÉDITOS==X===", font = "Arial 12 bold")
        lbl.grid(column = 0, row = 1)
        lbl = Label(newwindow, text="@vivianne_keys \n https://github.com/VivianneChaves", font="Arial 12")
        lbl.grid(column=0, row=3)




    window = Tk()
    window.title("Simulador de empréstimo")
    window.maxsize("700","800")
    photo = PhotoImage(file = 'imagem.png')
    lbl = Label(window, image = photo)
    lbl.grid(column = 0, row= 0)
    lbl = Label(window, text="Digite o valor que deseja pegar emprestado:", font = "Times 15")
    lbl.grid(column=0, row=3,)
    txt = Entry(window, width=36)
    txt.grid(column=0, row=4)
    lbl = Label(window, text="Em quantos meses deseja pagar?", font="Times 15")
    lbl.grid(column=0, row=5, )
    txt1 = Entry(window, width=36)
    txt1.grid(column=0, row=6)
    btn = Button(window, text="Enviar", command=enviar)
    btn.grid(column=0, row=11)
    btn = Button(window, text=" Sair ", command=exit)
    btn.grid(column=0, row=12)
    btn = Button(window, text="Sobre", command=JanelaCreditos)
    btn.grid(column=0, row=13)

    window.mainloop()