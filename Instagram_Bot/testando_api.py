from instagram_private_api import Client, ClientCompatPatch
from dotenv import dotenv_values
import time
import uuid


env = dotenv_values(".env")

# Substitua 'SEU_USUÁRIO' e 'SUA_SENHA' pelas suas credenciais do Instagram
username = env["username"]
password = env["password"]

# Criando um rank_token único com base no timestamp atual e um UUID
timestamp = int(time.time())
unique_identifier = f"{timestamp}_{uuid.uuid4()}"

api = Client(username, password)
results = api.tag_search('hashtag', rank_token=unique_identifier)
tag = results['results'][0] # Vamos pegar o primeiro resultado da busca
tag_name = tag['name']

media_items = api.tag_feed(tag_name, count=10) # Obtemos as 10 mídias mais recentes com a hashtag

for media in media_items:
    print(media['image_versions2']['candidates'][0]['url']) # Exibe a URL da imagem