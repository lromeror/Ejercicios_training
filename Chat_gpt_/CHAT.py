import openai
import os
import sys
import time
openai.api_key = "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"


# Esperar tiempo hasta que se genere todo y luego muestra
# pero si queremos que se vaya mostrando 
# un stream tener un archivo grande en un servidos y lo va enviando poco a pocos
chat_history = []
while True : 
    prompt = input("Ingresa tu pregunta : ")
    if prompt == "exit" :
        break
    else :
        chat_history.append({"role":"user","content":prompt})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages =[
                {
                    "role" : "user",
                    "content" : prompt
                }
            ],
            stream = True,
            #max_tokens = 100,
        )
        #print(response["choices"][0]["message"]["content"])
        collected_message =  []
        for chunk in response:
            chunk_message = chunk["choices"][0]["delta"]
            collected_message.append(chunk_message)
            full_reply_content = ''.join([m.get('content','')for m in collected_message])

        chat_history.append({"role":"assistant","content":full_reply_content}) 
        for char in full_reply_content:
            sys.stdout.write(char)
            sys.stdout.flush()  # Asegura que el carácter se imprime inmediatamente
            time.sleep(0.05)  # Ajusta este valor para cambiar la velocidad de "escritura"
        print()  


