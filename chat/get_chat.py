import requests
import json
import openai

# Inicialize a API do OpenAI
openai.api_key = "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"

def handle_message(update):
    message = update

    # Use o OpenAI para responder a mensagem
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"{message}\n",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    ).choices[0].text

    # Retorna a resposta gerada pela API do OpenAI
    return response


