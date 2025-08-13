# %%

import requests
import json
from tqdm import tqdm

import pandas as pd

# %%

ceps = ["09990240",
        "11740662",
        "11742660",
        "099460740",
        "015190000",
        ]

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:

        dados.append( resposta.json())
dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%
print(dados)

with open("ceps.json", "w", encoding='UTF-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

 # %%   