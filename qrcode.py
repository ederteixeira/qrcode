from tkinter import *
import pyqrcode

def gerador():
    criador = textoins.get()
    url = pyqrcode.create(criador)
    url.svg('qrcode.svg', scale=6)
    url.png('qrcode.png', scale=6)

app = Tk()
app.geometry("400x250")
app.title("Gerador QRCode")

texto = Label(app, text="Informe o site:")
texto.grid(column=0, row=0)

textoins = Entry(app)
textoins.grid(column=1, row=0)

botao =  Button(app, text="Gerar", command=gerador)
botao.grid(column=2, row=0)

app.mainloop()
