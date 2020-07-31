import http.server
import socketserver
import json
import requests

# Lista contendo as possíveis frases dos usuários que interagirem com o bot
phrases = [
    ("/start", "Olá! Seja bem-vindo ao Suporte do Banco Carrefour. Para iniciar digite: TRANSACOES"),
    ("transações", "Você deseja saber o limite das suas transações? Por favor, responda SIM ou NAO"),
    ("transacoes", "Você deseja saber o limite das suas transações? Por favor, responda SIM ou NAO"),
    ("sim", "Seu plano contempla 10 transações diárias."),
    ("nao", "Agradecemos o contato"),
    ("não", "Agradecemos o contato"),
]

# Função para receber texto do usuário
def getResponse(text_user):
    for phrase in phrases:
        # Importante transformar tudo para minúsculo
        if text_user.lower() == phrase[0]:
            return phrase[1]
    return "Não consegui entender. Por gentileza, para iniciar digite: TRANSACOES"

# Classe para criação do handler das requests que virão da API do Telegram
class TelegramHandler(http.server.SimpleHTTPRequestHandler):

    # Função para utilizar o método POST
    def do_POST(self):
        info_post = self.rfile.read(int(self.headers['Content-Length']))
        info_json = json.loads(info_post)

        chat_id = info_json['message']['from']['id']
        text_user = info_json['message']['text']

        text_bot = getResponse(text_user)

        urlSend = "https://api.telegram.org/bot1315839851:AAFR3huE8AXbTcV4ssk8ZaO2W6O90hWjsXM/sendMessage"

        # Criando a requisição por método POST contendo o ID do chat e a frase do bot
        req = requests.post(url=urlSend, params={'chat_id': chat_id, 'text': text_bot})

        if req.status_code == 200:
            self.send_response(200)
            self.end_headers()

    # Funçao para utilizar o método GET
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

# Configurando servidor depois de ter utilizado o Ngrok na porta 8000 pra escutar as requisições
server = socketserver.TCPServer(('0.0.0.0', 8000), TelegramHandler)

# Servidor sendo executado sem interrupção
server.serve_forever()