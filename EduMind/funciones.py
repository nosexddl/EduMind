import os
from datetime import datetime
from PyPDF2 import PdfReader

def guardar_chat(contenido):
    carpeta = "chats"
    os.makedirs(carpeta, exist_ok=True)
    nombre_archivo = datetime.now().strftime("chat_%Y%m%d_%H%M%S.txt")
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    with open(ruta_completa, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def leer_pdf(ruta):
    texto = ""
    lector = PdfReader(ruta)
    for pagina in lector.pages:
        texto += pagina.extract_text() + "\n"
    return texto.strip()
