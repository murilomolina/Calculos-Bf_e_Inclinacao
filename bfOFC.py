#processamento
calculo = False
while not calculo:
#Entrada de dados/correcao de virgula
    area_terreno = float(input('\nInsira a AREA DO TERRENO em m²: ').replace(',','.'))
    area_computavel = float(input('Insira a AREA COMPUTÁVEL em m²: ').replace(',','.'))
    valor_referencia = float(input('Insira o VALOR REFERENCIA: ').replace(',','.'))
    zona = int(input(f"Insira qual a zona desejada\nZona de Qualificação (1)\nZona de Reestruturação (2)\n"))
#varaiveis referentes ao processamento:
    cp = area_computavel/area_terreno
    fator_reducao = 0.8
    fmp = 5.0578    
    if zona == 1:
        ic = 0.4
        coeficiente_basico = 2.5
        cpc = round(cp - coeficiente_basico,2)
        bf = (area_terreno * valor_referencia * cpc * ic * fator_reducao) * fmp
    if zona == 2:
        ic = 0.33
        coeficiente_projeto = 3.0
        cpc = round(cp - coeficiente_projeto,2)
        bf = (area_terreno * valor_referencia * cpc * ic * fator_reducao) * fmp
    elif cp > coeficiente_basico or cp > coeficiente_projeto:
        print(f'\nRESULTADO OBTIDO:\nR$ {bf:.2f}\nCPC = {(cp):.2f}')
    elif cp < coeficiente_basico or coeficiente_projeto:
        print(f'\nResultado do CP menor que 2.5\nNão é necessario pagar a ODC!\nCPC = {(cp):.2f}')
    else:
        print('\nERRO! Zona invalida!!')
    encerrar = input('\nPara realizar outro calculo insira "c"\nPara encerrar o calculo digite "f"\n')
    if encerrar == ('c'):
        calculo = False
    if encerrar == ('f'):
        calculo = True
        print('TCHAU!!!!')