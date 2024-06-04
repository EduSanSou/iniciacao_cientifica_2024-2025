# abrir e fechar dataset para salvar as linhas em uma lista
with open ('data.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# verificar e armazenar as linhas corretas na lista linhas_corretas
linhas_corretas = []
for linha in linhas:
    valores = linha.split()
    if len(valores) == 8 and int(valores[3]) < 55:
        linhas_corretas.append(linha)

# salvar as linhas corretas em um novo arquivo .txt 
with open ('right_data.txt', 'w') as arquivo_saida:
     arquivo_saida.writelines(linhas_corretas)