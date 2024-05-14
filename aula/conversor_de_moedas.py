taxa_euro = 5.56
taxa_iene = 30.34
valor_real = float(input('Digite o valor em R$ '))
txt_euro = f'{valor_real / taxa_euro:.2f}'
txt_iene = f'{valor_real * taxa_iene:.2f}'
print(f'Euro: {txt_euro} | Iene: {txt_iene}')
