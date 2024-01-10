from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class calculoBF(App):
    def build(self):
        self.area_terreno_input = TextInput(multiline=False, input_type='number', hint_text='Área do Terreno (m²)')
        self.area_computavel_input = TextInput(multiline=False, input_type='number', hint_text='Área Computável (m²)')
        self.valor_referencia_input = TextInput(multiline=False, input_type='number', hint_text='Valor Referência')
        self.zona_input = TextInput(multiline=False, input_type='number', hint_text='Zona (1 ou 2)')

        self.result_label = Label(text='Resultado:')

        calculate_button = Button(text='Calcular', on_press=self.calculate)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.area_terreno_input)
        layout.add_widget(self.area_computavel_input)
        layout.add_widget(self.valor_referencia_input)
        layout.add_widget(self.zona_input)
        layout.add_widget(calculate_button)
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        area_terreno = float(self.area_terreno_input.text.replace(',', '.'))
        area_computavel = float(self.area_computavel_input.text.replace(',', '.'))
        valor_referencia = float(self.valor_referencia_input.text.replace(',', '.'))
        zona = int(self.zona_input.text)

        cp = area_computavel / area_terreno
        fator_reducao = 0.8
        fmp = 5.0578
        if zona == 1:
            ic = 0.4
            coeficiente_basico = 2.5
            cpc = round(cp - coeficiente_basico, 2)
            bf = (area_terreno * valor_referencia * cpc * ic * fator_reducao) * fmp
        elif zona == 2:
            ic = 0.33
            coeficiente_projeto = 3.0
            cpc = round(cp - coeficiente_projeto, 2)
            bf = (area_terreno * valor_referencia * cpc * ic * fator_reducao) * fmp
        else:
            self.result_label.text = '\nERRO! Zona inválida!!'
            return

        if cp > coeficiente_basico or cp > coeficiente_projeto:
            self.result_label.text = f'\nRESULTADO OBTIDO:\nR$ {bf:.2f}\nCPC = {(cp):.2f}'
        elif cp < coeficiente_basico or coeficiente_projeto:
            self.result_label.text = f'\nResultado do CP menor que 2.5\nNão é necessário pagar a ODC!\nCPC = {(cp):.2f}'

if __name__ == '__main__':
    calculoBF().run()