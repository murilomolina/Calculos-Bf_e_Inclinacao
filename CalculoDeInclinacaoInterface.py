from tkinter import *
#calculos
def comecar():
    var_calculada = opcao.get()
    if var_calculada == 'c':
        i = float(input_inclinacao.get().replace(',', '.'))
        h = float(input_altura.get().replace(',', '.'))
        c = (h * 100) / i
        texto_formula['text'] = f'O valor do comprimento é: {c:.2f} metros'
    elif var_calculada == 'i':
        c = float(input_comprimento.get().replace(',', '.'))
        h = float(input_altura.get().replace(',', '.'))
        i = (h * 100) / c
        texto_formula['text'] = f'O valor de inclinação é: {i:.2f}%'
    elif var_calculada == 'h':
        i = float(input_inclinacao.get().replace(',', '.'))
        c = float(input_comprimento.get().replace(',', '.'))
        h = (i * c) / 100
        texto_formula['text'] = f'O valor de altura é: {h:.2f} metros'
    else:
        texto_formula['text'] = 'Variável não reconhecida!!'
    calculo_ok.set(True)
# Criação da janela principal
janela = Tk()
janela.title("Cálculo de inclinação")
# Criação dos elementos gráficos
texto_orientacao = Label(janela, text='Escolha a variável que deseja calcular:')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)
# Variável para guardar a opção selecionada
opcao = StringVar()
#escolher a opção
opcao_comprimento = Radiobutton(janela, text='Comprimento (c)', variable=opcao, value='c')
opcao_comprimento.grid(column=0, row=1, padx=10, pady=5, sticky=W)
opcao_inclinacao = Radiobutton(janela, text='Inclinação (i)', variable=opcao, value='i')
opcao_inclinacao.grid(column=0, row=2, padx=10, pady=5, sticky=W)
opcao_altura = Radiobutton(janela, text='Altura (h)', variable=opcao, value='h')
opcao_altura.grid(column=0, row=3, padx=10, pady=5, sticky=W)

texto_comprimento = Label(janela, text='Comprimento (c):')
texto_comprimento.grid(column=1, row=1, padx=10, pady=5)
input_comprimento = Entry(janela)
input_comprimento.grid(column=2, row=1, padx=10, pady=5)

texto_inclinacao = Label(janela, text='Inclinação (i):')
texto_inclinacao.grid(column=1, row=2, padx=10, pady=5)
input_inclinacao = Entry(janela)
input_inclinacao.grid(column=2, row=2, padx=10, pady=5)

texto_altura = Label(janela, text='Altura (h):')
texto_altura.grid(column=1, row=3, padx=10, pady=5)
input_altura = Entry(janela)
input_altura.grid(column=2, row=3, padx=10, pady=5)

botao_comecar = Button(janela, text='Calcular', command=comecar)
botao_comecar.grid(column=2, row=4, padx=10, pady=10)

texto_formula = Label(janela, text='')
texto_formula.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

#Variável que controla a saída do loop
calculo_ok = BooleanVar()
calculo_ok.set(False)

#Loop principal da janela
while not calculo_ok.get():
    janela.update()

janela.mainloop()
