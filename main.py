import openai 
import config

#llamada a la api_key
openai.api_key = config.api_key

#contexto del asistente
messages=[{"role": "system", "content": "eres un asistente muy util"}]

#pregunta al asistente
while True:

    content = input("Que pregunta tienes? ")

    if content == 'salir':
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    response_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_content})

    print (response_content) 