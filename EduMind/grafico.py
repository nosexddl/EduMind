import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from inteligencia_artificial import responder
from funciones import guardar_chat, leer_pdf  # Asegúrate de que esto exista

def enviar_pregunta():
    pregunta = entrada.get()
    if not pregunta.strip():
        messagebox.showwarning("Advertencia", "Por favor, escribe una pregunta.")
        return
    respuesta = responder(pregunta)
    texto_respuesta.insert(tk.END, f"\n👤 Usuario: {pregunta}\n🤖 IA: {respuesta}\n")
    texto_respuesta.see(tk.END)
    entrada.delete(0, tk.END)

def guardar_chat_en_txt():
    # Guarda todo el contenido del área de texto
    contenido = texto_respuesta.get("1.0", "end").strip()
    if contenido:
        guardar_chat(contenido)

def analizar_pdf():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if not archivo:
        return
    contenido = leer_pdf(archivo)
    entrada.delete(0, tk.END)
    entrada.insert(0, contenido[:500])  # puedes ajustar el número si el texto es muy largo

ventana = tk.Tk()
ventana.title("Asistente Escolar IA (Offline)")
ventana.geometry("700x700")  # Subí un poco el alto por los botones
ventana.configure(bg="#0f111a")

# Título personalizado
titulo = tk.Label(ventana, text="Asistente Escolar IA", font=("Segoe UI", 20, "bold"), fg="white", bg="#0f111a")
titulo.pack(pady=10)

# Caja de conversación
texto_respuesta = scrolledtext.ScrolledText(
    ventana, wrap=tk.WORD, width=80, height=25,
    bg="#1e1e2f", fg="#e0e0e0", insertbackground="white",
    font=("Consolas", 12), borderwidth=0
)
texto_respuesta.pack(padx=20, pady=10, fill="both", expand=True)

# Frame para entrada y botón
frame_entrada = tk.Frame(ventana, bg="#0f111a")
frame_entrada.pack(pady=10)

# Entrada de pregunta
entrada = tk.Entry(frame_entrada, width=60, font=("Segoe UI", 13), bg="#2b2b3d", fg="white", insertbackground="white", borderwidth=2, relief="flat")
entrada.grid(row=0, column=0, padx=10)

# Botón de enviar
boton = tk.Button(
    frame_entrada, text="Enviar", command=enviar_pregunta,
    bg="#0078d7", fg="white", activebackground="#005a9e",
    font=("Segoe UI", 11, "bold"), relief="flat", padx=20, pady=5
)
boton.grid(row=0, column=1)

# Nuevo Frame para los botones adicionales
frame_botones = tk.Frame(ventana, bg="#0f111a")
frame_botones.pack(pady=10)

# Botón: Guardar Chat
btn_guardar = tk.Button(
    frame_botones, text="Guardar Chat", command=guardar_chat_en_txt,
    bg="#28a745", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=5
)
btn_guardar.grid(row=0, column=0, padx=10)

# Botón: Leer PDF
btn_pdf = tk.Button(
    frame_botones, text="Leer PDF", command=analizar_pdf,
    bg="#17a2b8", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=15, pady=5
)
btn_pdf.grid(row=0, column=1, padx=10)

ventana.mainloop()
