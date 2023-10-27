import openai
import os
import sys
import time
openai.api_key = "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"
def analizar_ejercicio(ejercicio):
    # Paso 1: Identificar el contexto del ejercicio
    contexto = identificar_contexto(ejercicio)
    
    # Paso 2: Buscar un ejercicio similar
    ejercicio_similar = buscar_ejercicio_similar(contexto)
    
    # Paso 3: Generar la solución y explicación del ejercicio original
    respuesta = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Explica y resuelve el siguiente ejercicio de Python:\n\n{ejercicio}",
      temperature=0.5,
      max_tokens=150
    )
    solucion = respuesta.choices[0].text.strip()
    
    # Paso 4: Componer la respuesta final
    respuesta_final = f"Solución y Explicación: {solucion}\nContexto: {contexto}\nEjercicio Similar: {ejercicio_similar}"
    
    return respuesta_final

def identificar_contexto(pregunta):
    # Palabras clave asociadas a diferentes estructuras de datos
    palabras_listas = ["lista", "elementos", "índices", "orden"]
    palabras_diccionarios = ["diccionario", "claves", "valores", "mapeo"]
    palabras_tuplas = ["tupla", "inmutable", "ordenada"]
    palabras_conjuntos = ["conjunto", "únicos", "sin orden"]
    palabras_arreglos = ["arreglo", "numpy", "índices"]
    
    # Convertir la pregunta a minúsculas para hacer la comparación insensible a mayúsculas
    pregunta = pregunta.lower()
    
    # Inicializar el contexto
    contexto = []
    
    # Identificar el contexto basado en las palabras clave
    if any(palabra in pregunta for palabra in palabras_listas):
        contexto.append("listas")
    if any(palabra in pregunta for palabra in palabras_diccionarios):
        contexto.append("diccionarios")
    if any(palabra in pregunta for palabra in palabras_tuplas):
        contexto.append("tuplas")
    if any(palabra in pregunta for palabra in palabras_conjuntos):
        contexto.append("conjuntos")
    if any(palabra in pregunta for palabra in palabras_arreglos):
        contexto.append("arreglos")
    
    # Convertir la lista de contexto a una cadena de texto para el retorno
    resultado = ", ".join(contexto) if contexto else "No se pudo identificar el contexto"
    
    return resultado

def buscar_ejercicio_similar(contexto, ejercicio_original):
    
    
    # Formular la pregunta para OpenAI
    pregunta = f"Basado en el siguiente contexto: {contexto}, genera un ejercicio similar a: {ejercicio_original}"
    
    
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
            max_tokens = 100,
        )
        
    # Extraer y retornar el texto del ejercicio generado
    ejercicio_generado = response["choices"][0]["message"]["content"].text.strip()
    return ejercicio_generado


# Esperar tiempo hasta que se genere todo y luego muestra
# pero si queremos que se vaya mostrando 
# un stream tener un archivo grande en un servidos y lo va enviando poco a pocos
chat_history = []
while True : 
    prompt = input("Ingresa tu pregunta : ")
    if prompt == "exit" :
        break
    else :
        analizar_ejercicio(prompt)

#        chat_history.append({"role":"user","content":prompt})
#        response = openai.ChatCompletion.create(
#            model = "gpt-3.5-turbo",
#            messages =[
#                {
#                    "role" : "user",
#                    "content" : prompt
#                }
#            ],
#            stream = True,
#            #max_tokens = 100,
#        )
#        #print(response["choices"][0]["message"]["content"])
#        collected_message =  []
#        for chunk in response:
#            chunk_message = chunk["choices"][0]["delta"]
#            collected_message.append(chunk_message)
#            full_reply_content = ''.join([m.get('content','')for m in collected_message])
#
#        chat_history.append({"role":"assistant","content":full_reply_content}) 
#        for char in full_reply_content:
#            sys.stdout.write(char)
#            sys.stdout.flush()  # Asegura que el carácter se imprime inmediatamente
#            time.sleep(0.05)  # Ajusta este valor para cambiar la velocidad de "escritura"
#        print()  


