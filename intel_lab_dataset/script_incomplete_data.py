# abrir e fechar dataset para salvar as linhas em uma lista
with open ('data.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# verificar e armazenar as que sao incompletas na lista linhas_lixo
linhas_incompletas = []
for linha in linhas:
    valores = linha.split()
    if len(valores) != 8:
        linhas_incompletas.append(linha)
    #elif len(valores) >= 4 and int(valores[3]) > 54:
        #linhas_lixo.append(linha)     

# salvar as linhas incompletas em um novo arquivo .txt 
with open ('incomplete_data.txt', 'w') as arquivo_saida:
     arquivo_saida.writelines(linhas_incompletas)