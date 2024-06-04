# Abrir o arquivo original para leitura
with open('data.txt', 'r') as arquivo_entrada:
    # Ler todas as linhas do arquivo
    linhas = arquivo_entrada.readlines()

for i in range(1,55):
    #Lista para armazenar as linhas que atendem ao critério
    linhas_selecionadas = []
    
    # Verificar cada linha
    for linha in linhas:
        # Dividir a linha em valores separados por espaço em branco
        valores = linha.split()
        # Verificar se a linha tem oito valores e se o quarto valor é "i"
        if len(valores) == 8 and valores[3] == str(i):
            linhas_selecionadas.append(linha)

    # Abrir um novo arquivo para escrita
    with open('data_device_moteid_' + str(i) + '.txt', 'w') as arquivo_saida:
        # Escrever as linhas selecionadas no novo arquivo
        arquivo_saida.writelines(linhas_selecionadas)