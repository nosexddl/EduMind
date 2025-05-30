from gpt4all import GPT4All

# Cambia esta ruta por donde tengas tu archivo .gguf
modelo_ruta = "mistral-7b-openorca.gguf2.Q4_0.gguf"  
# Ejemplo: modelo_ruta = "C:/Users/TuUsuario/Descargas/mistral-7b-instruct.gguf"

# Carga el modelo en modo offline (no buscará ni descargará nada)
modelo = GPT4All(modelo_ruta, allow_download=False)

def responder(pregunta):
    with modelo.chat_session() as sesion:
        respuesta = sesion.generate(pregunta)
        return respuesta
