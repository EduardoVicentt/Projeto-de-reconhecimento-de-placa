from tkinter import *
from tkinter.filedialog import askopenfilename
from typing import Any
import cv2
import imutils
import pytesseract
import numpy as np

#Para se usar o Tesseract no Python, temos que indicar onde o mesmo esta instalado juntamente com seu executavel
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread('imagens/img.png')

# função para selecionar um arquivo do pc
def ler():
    global filename
    filename = askopenfilename()  # Isto te permite selecionar um arquivo
    texto_resposta = Label(janela2, text=filename, font=("Arial", 10))
    texto_resposta.grid(column=0, row=3, padx=10, pady=10)
    texto_resposta.config(bg='#004d66', fg='#FFFFFF')
    # botão para ler a imagem selecionada
    botao2_main = Button(janela2, text="Executar Leitura", command=rp, font=("Arial", 10))
    botao2_main.grid(column=0, row=4, padx=10, pady=10)
    botao2_main.config(bg='#808080', fg='#FFFFFF')

"""def main():
    nome_arquivo = "C:\\Users\\milim\\OneDrive\\Documentos\\NetBeansProjects\\Condominios\\src\\static\\placa.txt"
   

    placa = rp()

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(placa)

    print("Arquivo criado com sucesso!")"""
    
def rp():
    img = cv2.imread(filename)

    kernel = np.ones((3, 3), np.uint8)

    img = imutils.resize(img, width=520)

    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("imagem original", img)

    _, bin = cv2.threshold(cinza, 70, 255, cv2.THRESH_BINARY)

    #cv2.imshow("bin", bin)

    desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
    #cv2.imshow("desfoque", desfoque)

    dilatacao = cv2.erode(bin, kernel, iterations=1)
    #cv2.imshow("dilatacao", dilatacao)

    erosao = cv2.dilate(dilatacao, kernel, iterations=1)
    #cv2.imshow("erosao", erosao)

    con = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
    text = pytesseract.image_to_string(erosao, lang='eng', config=con)

    print("Number is : ", text)
    texto_resposta = Label(janela2, text=text, font=("Arial", 12))
    texto_resposta.grid(column=0, row=6, padx=10, pady=10)
    texto_resposta.config(bg='#004d66', fg='#FFFFFF')
    nome_arquivo = "C:\\Users\\milim\\OneDrive\\Documentos\\NetBeansProjects\\Condominios\\src\\static\\placa.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(text)

    print("Arquivo criado com sucesso!")

# janela principal
janela2 = Tk()
janela2.minsize(450, 300)
janela2.maxsize(450, 400)
janela2.title("S.A.R.A layout")
janela2.config(bg='#004d66')

logo_main = Label(janela2, text="S.A.R.A", font=("Arial", 25))
logo_main.grid(column=0, row=0, padx=160, pady=0)
logo_main.config(bg='#004d66', fg='#FFFFFF')

texto_main = Label(janela2, text=" ", font=("Arial", 20))
texto_main.grid(column=0, row=1, padx=50, pady=10)
texto_main.config(bg='#004d66', fg='#FFFFFF')

# botão para selecionar a imagem
botao_main = Button(janela2, text="Selecionar Placa", command=ler, font=("Arial", 10))
botao_main.grid(column=0, row=1, padx=10, pady=10)
botao_main.config(bg='#808080', fg='#FFFFFF')

# botão ok
def ok():
    janela2.destroy()

botao3_main = Button(janela2, text="OK", command=ok, font=("Arial", 10))
botao3_main.grid(column=0, row=7, padx=10, pady=10)
botao3_main.config(bg='#009900', fg='#FFFFFF')

# espaço invisível
textoinv = Label(janela2, text=" ", font=("Arial", 20))
textoinv.grid(column=0, row=6, padx=50, pady=0)
textoinv.config(bg='#004d66', fg='#FFFFFF')

janela2.mainloop()
# fim da primeira janela