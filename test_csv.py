import csv

with open('informe_epidemiologico_13_03_2021_geral.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ';')
    numero_linhas = 0
    for row in csv_reader:
        if numero_linhas == 0:
            print(f'Nome das colunas são {", ".join(row)}')
        numero_linhas += 1
    print('Leu '+str(numero_linhas)+' linhas')