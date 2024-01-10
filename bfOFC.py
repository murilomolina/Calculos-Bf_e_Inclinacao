import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox


class CalculoBF(QWidget):
    def __init__(self):
        super().__init__()

        self.area_terreno_input = QLineEdit(self)
        self.area_terreno_input.setPlaceholderText('Área do Terreno (m²)')

        self.area_computavel_input = QLineEdit(self)
        self.area_computavel_input.setPlaceholderText('Área Computável (m²)')

        self.valor_referencia_input = QLineEdit(self)
        self.valor_referencia_input.setPlaceholderText('Valor Referência')

        self.zona_input = QLineEdit(self)
        self.zona_input.setPlaceholderText('Zona (1 ou 2)')

        self.result_textedit = QTextEdit(self)
        self.result_textedit.setPlaceholderText('Resultado:')
        self.result_textedit.setReadOnly(True)

        calculate_button = QPushButton('Calcular', self)
        calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout(self)
        layout.addWidget(self.area_terreno_input)
        layout.addWidget(self.area_computavel_input)
        layout.addWidget(self.valor_referencia_input)
        layout.addWidget(self.zona_input)
        layout.addWidget(calculate_button)
        layout.addWidget(self.result_textedit)

    def calculate(self):
        try:
            area_terreno = float(self.area_terreno_input.text().replace(',', '.'))
            area_computavel = float(self.area_computavel_input.text().replace(',', '.'))
            valor_referencia = float(self.valor_referencia_input.text().replace(',', '.'))
            zona = int(self.zona_input.text())

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
                self.result_textedit.setPlainText('\nERRO! Zona inválida!!')
                return

            if cp > coeficiente_basico or cp > coeficiente_projeto:
                result_text = f'\nRESULTADO OBTIDO:\nR$ {bf:.2f}\n\nCPC = {(cp):.2f}'
            elif cp < coeficiente_basico or coeficiente_projeto:
                result_text = f'\nResultado do CP menor que 2.5\nNão é necessário pagar a ODC!\nCPC = {(cp):.2f}'

            self.result_textedit.setPlainText(result_text)

        except ValueError:
            QMessageBox.warning(self, 'Erro de Entrada', 'Por favor, insira valores válidos nos campos.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculoBF()
    window.show()
    sys.exit(app.exec_())
