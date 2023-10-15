# formato
# {"prompt": "<prompt text>", "completion": "<ideal generated text>"}

import pandas as pd 
import json

data = {
    "prompt": [],
    "completion": []
}
with open("Ejercicios/resoluciones.txt", 'r') as file:
    texto = file.read().replace("#","")
    l_texto = texto.split('"""')
    # El primero es ' '
    for i in range(1,len(l_texto),2):
        data["prompt"].append(l_texto[i])
        data["completion"].append(l_texto[i+1])

df = pd.DataFrame(data)

with open('Ejercicios/resoluciones.jsonl', 'w') as file:
    for i, row in df.iterrows():
        entry = row.to_dict()
        json.dump(entry, file)
        file.write('\n')

