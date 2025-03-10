import paho.mqtt.client as mqtt
import time
import json

endereco_dataset="/home/insert/MQTT/data.txt"
topico="/home/sensors2"
cliente = mqtt.Client(client_id="publisher2",protocol=mqtt.MQTTv311,clean_session=True,transport="tcp")
conexao = cliente.connect(host="192.168.1.8",port=1883,keepalive=60)

with open(endereco_dataset,"r") as file:
    for line in file:
        linha_separada=line.split()
        temperature = float(linha_separada[4])
        humidity = float(linha_separada[5])
        light = float(linha_separada[6])
        voltage = float(linha_separada[7])
        mensagem=json.dumps({"t":temperature,"h":humidity,"l":light,"v":voltage})
        cliente.publish(topic=topico,payload=mensagem,qos=0,retain=False)
        time.sleep(0.5)
        print(mensagem)
print("fim")