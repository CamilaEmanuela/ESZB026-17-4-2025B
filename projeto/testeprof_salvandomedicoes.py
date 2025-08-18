#!/usr/bin/python3

import serial
import time


porta_serial = '/dev/ttyACM0'
velocidade = 115200

# Nome do arquivo onde os dados serão salvos.
nome_arquivo = '/var/www/html/dados_arduino.txt'
#nome_arquivo = '/home/pi/dados_arduino.txt'

try:
    # Tenta abrir a conexão serial.
    conexaoSerial = serial.Serial(porta_serial, velocidade, timeout=1)
    # Aguarda 2 segundos para o Arduino reiniciar.
    time.sleep(2)
    print(f"Conectado à porta serial {porta_serial}. Coletando 20 dados...")

    # Abre o arquivo no modo de escrita ('w'). O arquivo será criado ou substituído.
    with open(nome_arquivo, 'w') as arquivo:
        for i in range(20):
            # Lê uma linha da porta serial, que deve terminar com '\n'.
            dado_recebido = conexaoSerial.readline()
            
            # Decodifica os bytes para string e remove espaços e quebras de linha.
            dado_string = dado_recebido.decode('utf-8').strip()

            # Tenta converter a string para um número inteiro.
            try:
                valor = int(dado_string)
                print(f"Dado {i+1}: {valor}")
                
                # Salva o valor no arquivo, seguido de uma quebra de linha.
                arquivo.write(str(valor) + '\n')
            
            except ValueError:
                # Se a conversão falhar, exibe uma mensagem de erro.
                print(f"Erro: Não foi possível converter o dado '{dado_string}' para inteiro.")
            
            # Pausa por um pequeno intervalo para não sobrecarregar a porta serial.
            time.sleep(0.1)

    print(f"\nColeta de dados finalizada. Os dados foram salvos em '{nome_arquivo}'.")

except serial.SerialException as e:
    # Trata erros de conexão, como a porta não existir.
    print(f"Erro de conexão serial: {e}")
except Exception as e:
    # Trata outros erros inesperados.
    print(f"Ocorreu um erro: {e}")
finally:
    # Garante que a conexão seja fechada, mesmo se houver um erro.
    if 'conexaoSerial' in locals() and conexaoSerial.is_open:
        conexaoSerial.close()
        print("Conexão serial fechada.")
