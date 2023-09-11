import requests
import json
import openai

# Inicialize a API do OpenAI
openai.api_key = ""

# Defina a função para enviar mensagens ao Telegram
def send_message(chat_id, text):
    url = f"https://api.telegram.org/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

# Defina a função principal que será executada ao receber mensagens do Telegram
def handle_message(update):
    chat_id = update["message"]["chat"]["id"]
    message = update["message"]["text"]

    # Use o OpenAI para responder a mensagem
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"{message}\n",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    ).choices[0].text

    # Envie a resposta ao Telegram
    send_message(chat_id, response)

# Defina a URL para receber atualizações do Telegram
url = "https://api.telegram.org/etUpdates"

# Execute o loop infinito para receber atualizações do Telegram
def get():
    while True:
        response = requests.get(url).json()
        print(response["result"])
        if 'CHAT' in response["result"]:
            for update in response["result"]:
                print(update)
                handle_message(update)
    
