# ChatBot Banco Carrefour

ChatBot criado para o TechChallenge do Banco Carrefour com Python na versão 3.6.9.

Para executar a aplicação, clone este repositório.

Certifique-se de instalar a biblioteca ***requests*** através do pip em seu ambiente de desenvolvimento.

```console
user@machine:~$ pip3 install requests
```

Agora baixe a versão do **Ngrok** para o seu sistema operacional e descompacte o mesmo para uma pasta.

Na sequência, execute na sua distro Linux:

```console
user@machine:~$ ./ngrok http 8000
```
Isso irá apontar a porta 8000 da sua máquina para a URL que estiver presente no campo **forward** que o Ngrok lhe apresentar.

Adicione essa URL no final do endereço abaixo pois se trata da API do Telegram para setar o webhook:

https://api.telegram.org/bot1315839851:AAFR3huE8AXbTcV4ssk8ZaO2W6O90hWjsXM/setWebhook?url=

Por último, execute o script e teste a aplicação com:

```bash
user@machine:~$ python3 main.py
