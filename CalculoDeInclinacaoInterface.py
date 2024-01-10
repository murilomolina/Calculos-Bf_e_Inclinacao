from tkinter import *
from tkinter import ttk, messagebox

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 30

        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def validate_numeric_input(value, action):
    if action == '1':
        return value.replace(',', '').replace('.', '').isdigit() or value == ""
    return True

def comecar():
    var_calculada = opcao.get()
    try:
        if var_calculada == 'c':
            i = float(input_inclinacao.get().replace(',', '.'))
            h = float(input_altura.get().replace(',', '.'))
            c = (h * 100) / i
            texto_formula['text'] = f'O valor do comprimento é: {c:.6f} metros'
        elif var_calculada == 'i':
            c = float(input_comprimento.get().replace(',', '.'))
            h = float(input_altura.get().replace(',', '.'))
            i = (h * 100) / c
            texto_formula['text'] = f'O valor de inclinação é: {i:.6f}%'
        elif var_calculada == 'h':
            i = float(input_inclinacao.get().replace(',', '.'))
            c = float(input_comprimento.get().replace(',', '.'))
            h = (i * c) / 100
            texto_formula['text'] = f'O valor de altura é: {h:.6f} metros'
        else:
            raise ValueError("Variável não reconhecida!!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    
    calculo_ok.set(True)

janela = Tk()
janela.title("Cálculo de inclinação")

texto_orientacao = Label(janela, text='Escolha a variável que deseja calcular:')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

opcao = StringVar()

opcao_comprimento = Radiobutton(janela, text='Comprimento (c)', variable=opcao, value='c')
opcao_comprimento.grid(column=0, row=1, padx=10, pady=5, sticky=W)
Tooltip(opcao_comprimento, 'Calcular Comprimento')

opcao_inclinacao = Radiobutton(janela, text='Inclinação (i)', variable=opcao, value='i')
opcao_inclinacao.grid(column=0, row=2, padx=10, pady=5, sticky=W)
Tooltip(opcao_inclinacao, 'Calcular Inclinação')

opcao_altura = Radiobutton(janela, text='Altura (h)', variable=opcao, value='h')
opcao_altura.grid(column=0, row=3, padx=10, pady=5, sticky=W)
Tooltip(opcao_altura, 'Calcular Altura')

texto_comprimento_instrucao = Label(janela, text='Insira o comprimento (c):')
texto_comprimento_instrucao.grid(column=1, row=1, padx=10, pady=5, sticky=E)

texto_inclinacao_instrucao = Label(janela, text='Insira a inclinação (i):')
texto_inclinacao_instrucao.grid(column=1, row=2, padx=10, pady=5, sticky=E)

texto_altura_instrucao = Label(janela, text='Insira a altura (h):')
texto_altura_instrucao.grid(column=1, row=3, padx=10, pady=5, sticky=E)

input_comprimento = Entry(janela, validate='key', validatecommand=(validate_numeric_input, '%P', '%d'))
input_comprimento.grid(column=2, row=1, padx=10, pady=5)

input_inclinacao = Entry(janela, validate='key', validatecommand=(validate_numeric_input, '%P', '%d'))
input_inclinacao.grid(column=2, row=2, padx=10, pady=5)

input_altura = Entry(janela, validate='key', validatecommand=(validate_numeric_input, '%P', '%d'))
input_altura.grid(column=2, row=3, padx=10, pady=5)

botao_comecar = Button(janela, text='Calcular', command=comecar)
botao_comecar.grid(column=2, row=4, padx=10, pady=10, columnspan=2)

texto_formula = Label(janela, text='')
texto_formula.grid(column=0, row=5, columnspan=4, padx=10, pady=10)

calculo_ok = BooleanVar()
calculo_ok.set(False)

while not calculo_ok.get():
    janela.update()

janela.mainloop()
