from tkinter import *
from tkinter import messagebox
import tkinter as tk

def calcular():
    try:
        comprimento = float(input_comprimento.get().replace(",",".")) if input_comprimento.get() else None
        inclinacao = float(input_inclinacao.get().replace(",",".")) if input_inclinacao.get() else None
        altura = float(input_altura.get().replace(",",".")) if input_altura.get() else None

        if comprimento is None and inclinacao is not None and altura is not None:
            comprimento = (altura * 100) / inclinacao
            texto_formula['text'] = f'Comprimento (c): {comprimento:.6f} metros'
            texto_dados_complementares['text'] = f'Altura (h): {altura:.6f} metros\nInclinação (i): {inclinacao:.6f} %'

        elif inclinacao is None and comprimento is not None and altura is not None:
            inclinacao = (altura * 100) / comprimento
            texto_formula['text'] = f'Inclinação (i): {inclinacao:.6f}%'
            texto_dados_complementares['text'] = f'Altura (h): {altura:.6f} metros\nComprimento (c): {comprimento:.6f} metros'

        elif altura is None and comprimento is not None and inclinacao is not None:
            altura = (inclinacao * comprimento) / 100
            texto_formula['text'] = f'Altura (h): {altura:.6f} metros'
            texto_dados_complementares['text'] = f'Inclinação (i): {inclinacao:.6f} metros\nComprimento (c): {comprimento:.6f} metros'
        else:
            raise ValueError("Forneça dois valores para calcular o terceiro.")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def limpar_campos():
    input_comprimento.delete(0, END)
    input_inclinacao.delete(0, END)
    input_altura.delete(0, END)

janela = Tk()
janela.title("Cálculo de inclinação")

# layout mais responsivo
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

texto_info = Label(janela, text='Calcular automaticamente os campos em branco.', font=('Arial', 10))
texto_info.grid(column=0, row=0, columnspan=2, pady=10)

texto_comprimento_instrucao = Label(janela, text='Insira o comprimento (c):')
texto_comprimento_instrucao.grid(column=0, row=1, padx=10, pady=5, sticky=E)

texto_inclinacao_instrucao = Label(janela, text='Insira a inclinação (i):')
texto_inclinacao_instrucao.grid(column=0, row=2, padx=10, pady=5, sticky=E)

texto_altura_instrucao = Label(janela, text='Insira a altura (h):')
texto_altura_instrucao.grid(column=0, row=3, padx=10, pady=5, sticky=E)

input_comprimento = Entry(janela)
input_comprimento.grid(column=1, row=1, padx=10, pady=5, sticky=W+E)

input_inclinacao = Entry(janela)
input_inclinacao.grid(column=1, row=2, padx=10, pady=5, sticky=W+E)

input_altura = Entry(janela)
input_altura.grid(column=1, row=3, padx=10, pady=5, sticky=W+E)

botao_calcular = Button(janela, text='Calcular', command=calcular, bg="light green", bd=4, relief=tk.RAISED)
botao_calcular.grid(column=0, row=4, padx=10, pady=10, sticky=W+E)

botao_limpar = Button(janela, text='Limpar', command=limpar_campos, bg="red", bd=4, relief=tk.RAISED)
botao_limpar.grid(column=1, row=4, padx=10, pady=10, sticky=W+E)

texto_formula = Label(janela, text='', font=('Arial', 12), bg="light grey")
texto_formula.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky=W+E)

texto_dados_complementares = Label(janela, text='', font=('Arial', 9))
texto_dados_complementares.grid(column=0, row=6, columnspan=2, padx=10, pady=10, sticky=W+E)

janela.rowconfigure(6, weight=1)

janela.mainloop()
