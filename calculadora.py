import tkinter as tk
import math
from tkinter import messagebox


def somar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 + num2}")
    except ValueError:
        resultado.config(text="Erro, digite apenas números")
        return

def subtrair():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 - num2}")
    except ValueError:
        resultado.config(text="Erro, digite apenas números")
        return

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 * num2}")
    except ValueError:
        resultado.config(text="Erro, digite apenas números")
        return
    
def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 / num2}")
    except ValueError:
        resultado.config(text="Erro, digite apenas números")
        return
    except ZeroDivisionError:
        resultado.config(text="Erro, divisão por zero")
        return 

def calculo_raiz():
    segundo_campo(False)
    try:
        num1 = float(entrada1.get())
        resultado.config(text=f"Resultado: {math.sqrt(num1)}")
    except ValueError:
        resultado.config(text="Erro, digite apenas números no primeiro campo")
        return

def segundo_campo(segundoativo=True):
    if segundoativo == True:
        entrada2.config(state="normal")
    else:
        entrada2.delete(0, tk.END)
        entrada2.config(state="disabled")

def limpar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="")
    segundo_campo(True)


janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("1200x800")
janela.config(bg="lightblue")

frame = tk.Frame(janela)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
frame.config(width=700, height=700, bg="lightblue")

label1 = tk.Label(frame, text="Digite o primeiro número:", font=("Helvetica", 16), bg="lightblue", fg="black")
label1.pack(pady=20)

entrada1 = tk.Entry(frame, font=("Helvetica", 16))
entrada1.pack(pady=10)

label2 = tk.Label(frame, text="Digite o segundo número:", font=("Helvetica", 16), bg="lightblue", fg="black")
label2.pack(pady=20)

entrada2 = tk.Entry(frame, font=("Helvetica", 16))
entrada2.pack(pady=10)

resultado = tk.Label(frame, text="", font=("Helvetica", 16), bg="lightblue", fg="black")
resultado.pack(pady=20)

soma = tk.Button(frame, text="Somar", command=somar, font=("Helvetica", 16))
soma.pack(pady=10)
soma.config(width=15)
soma.config(width=15)

subtracao = tk.Button(frame, text="Subtrair", command=subtrair, font=("Helvetica", 16))
subtracao.pack(pady=10)
subtracao.config(width=15)

multiplicacao = tk.Button(frame, text="Multiplicar", command=multiplicar, font=("Helvetica", 16))
multiplicacao.pack(pady=10)
multiplicacao.config(width=15)

divisao = tk.Button(frame, text="Dividir", command=dividir, font=("Helvetica", 16))
divisao.pack(pady=10)
divisao.config(width=15)

raiz = tk.Button(frame, text="Raiz Quadrada", command=calculo_raiz, font=("Helvetica", 16))
raiz.pack(pady=10)
raiz.config(width=15)

limpar = tk.Button(janela, text="Limpar", command=limpar, font=("Helvetica", 16))
limpar.place(relx=0.98, rely=0.98, anchor="se")
limpar.config(width=15)

janela.mainloop()