# iniciacao_cientifica_2024-2025
Repositório relacionado aos projetos de Iniciação Científica da estudante Beatriz Azevedo e do estudante Eduardo Souza, discentes da Universidade Federal da Bahia (UFBA), sob orientação de Adriana Ribeiro e Leobino Sampaio, envolvendo os temas de caracterização de datasets públicos e experimentação de aplicações IoT por meio de dispositivos de hardware programáveis. O projeto é resultado do Programa Institucional de Bolsas de Iniciação Científica (PIBIC) da UFBA com fomento da Fundação de Amparo à Pesquisa do Estado da Bahia (FAPESB).

O diretório intel_lab_dataset contém o dataset utilizado no projeto, assim como sua descrição, scripts utilizados, subconjuntos e demais arquivos relacionados. Segue uma breve descrição de cada um deles:

Intel Lab Data.pdf: página web que descreve o projeto que sintetizou o dataset;

data.zip: arquivo que contém o dataset original;

data_device_moteid.zip: arquivo que contém os registros corretos do dataset separados por dispositivo;

data_with_labels.zip: arquivo que contém o dataset original acrescido de campos na primeira linha;

dataset_exploration.ipynb: arquivo jupyter notebook utilizado para exploração do dataset;

incomplete_data.txt: arquivo que contém apenas as linhas incompletas do dataset original;

incomplete_data_with_labels.txt: arquivo que contém apenas as linhas incompletas do dataset original, acrescido de campos na primeira linha;

inconsistent_data.txt: arquivo que contém apenas as linhas do dataset original com identificação de dispositivo incoerente;

inconsistent_data_with_labels.txt: arquivo que contém apenas as linhas do dataset original com identificação de dispositivo incoerente, acrescido de campos na primeira linha;

right_data.zip: arquivo que contém apenas as linhas corretas do dataset original;

right_data_with_labels.zip: arquivo que contém apenas as linhas corretas do dataset original, acrescido de campos na primeira linha;

script_incomplete_data.py: código para gerar o arquivo incomplete_data.txt;

script_inconsistent_data.py: código para gerar o arquivo inconsistent_data.txt;

script_moteid_readings.py: código para gerar cada um dos arquivos contidos em data_device_moteid.zip;

script_right_data.py: código para gerar o arquivo contido em right_data.zip;

(observação: alguns arquivos foram comprimidos por conta do tamanho original)

O diretório sensor_scripts contém os scripts executados nos dispositivos-sensores para publicação de dados. Segue uma breve descrição de cada um deles:

script_mqtt_publisher_json_data.py: script para o dispositivo publicador do tópico /home/sensors

script_mqtt_publisher_2_json_data.py: script para o dispositivo publicador do tópico /home/sensors2
