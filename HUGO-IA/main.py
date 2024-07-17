from senha import APY_KEY
import requests
import json

headers = {"Authorization": f"Bearer {APY_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/completions"
requisicao = requests.get(link, headers=headers)
id_modelo = "gpt-3.5-turbo-instruct-0914"

corpo_msg = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "Escreva um email para meu chefe com o preço e precisao do dolar em 6 meses"}]
}

corpo_msg = json.dumps(corpo_msg)

requisicao = requests.post(link, headers=headers, data=corpo_msg)

print(requisicao.text)