#!/bin/bash

# Define o caminho para o arquivo de dados.
# Certifique-se de que este caminho está correto.
ARQUIVODADOS="/home/pi/ESZB026-17-4-2025B/projeto/dados_arduino.txt"


# --- Cabeçalhos HTTP ---
# Informa ao navegador que o conteúdo é HTML.
echo "Content-type: text/html"
# Linha em branco que separa os cabeçalhos do corpo.
echo ""

# --- Início do corpo da página HTML ---
echo '<!DOCTYPE html>'
echo '<HTML>'
echo '  <HEAD>'
echo '    <meta charset="UTF-8">'
echo '    <TITLE>Página CGI gerando figura</TITLE>'
echo '  </HEAD>'
echo '  <BODY style="background-color:#FFFFE0">'
echo '    <H1>Página teste CGI e figuras.</H1>'
echo '    Rodando coleta de medidas <br>'
echo '<pre>'
/usr/local/bin/testeprof_salvandomedicoes.py
echo '</pre>'
echo '<pre>'
cat /var/www/html/dados_arduino.txt
echo '</pre>'
echo '<br>logado como o usuário '
whoami
echo '.<br>'
echo '    <h2 >DADOS:</h2>'
echo '    <pre>'
# Exibe o conteúdo do arquivo de dados.
cat "$ARQUIVODADOS"
echo '    </pre>'
echo '    <br>'
echo '    <br>'
echo '    <h2 >IMAGENS:</h2>'
echo '    Referenciando a imagem como "/cgi-bin/script_grafico.cgi": <br>'
echo '    <img src="/cgi-bin/script_grafico.cgi">'
echo '    <br>'
echo '    Referenciando a imagem como "script_grafico.cgi": <br>'
echo '    <img src="script_grafico.cgi">'
echo '    <br>'
echo '  </BODY>'
echo '</HTML>'
