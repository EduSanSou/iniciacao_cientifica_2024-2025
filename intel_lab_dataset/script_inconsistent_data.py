# abrir e fechar dataset para salvar as linhas em uma lista
with open ('data.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# verificar e armazenar as que sao inconsistentes na lista linhas_inconsistentes
linhas_inconsistentes = []
for linha in linhas:
    valores = linha.split()
    if len(valores) == 8 and int(valores[3]) > 54:
        linhas_inconsistentes.append(linha)     

# salvar as linhas inconsistentes em um novo arquivo .txt 
with open ('inconsistent_data.txt', 'w') as arquivo_saida:
     arquivo_saida.writelines(linhas_inconsistentes)