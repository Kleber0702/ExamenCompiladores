import tkinter as tk
from tkinter import scrolledtext
from lexer import lexer

def analizar_lexico(entrada):
    lexer.lineno = 1  # Reiniciar el contador de líneas
    lexer.input(entrada)
    tokens = []
    errores = []
    token_count = {}  # Diccionario para contar los tokens

    for tok in lexer:
        if tok.type != 'UNKNOWN':
            tokens.append((tok.type, tok.value, tok.lineno))
            # Contador de tokens
            token_count.setdefault(tok.type, 0)
            token_count[tok.type] += 1
        elif tok.type == 'UNKNOWN':
            errores.append((f"Error léxico: Token no reconocido '{tok.value}'", tok.lineno))

    mostrar_resultados(tokens, errores)
    mostrar_conteo(token_count)

    return tokens, errores

def analizar_button_click():
    entrada_text = entrada.get("1.0", tk.END)
    tokens, errores = analizar_lexico(entrada_text)

def mostrar_resultados(tokens, errores):
    resultado_text = ""
    for token in tokens:
        resultado_text += f"{token[0]}: {token[1]} (Línea {token[2]})\n"

    resultado_textbox.config(state=tk.NORMAL)
    resultado_textbox.delete('1.0', tk.END)
    resultado_textbox.insert(tk.END, resultado_text)
    resultado_textbox.config(state=tk.DISABLED)

def mostrar_conteo(token_count):
    conteo_text = "Conteo de tokens:\n"
    for token_type, count in token_count.items():
        conteo_text += f"{token_type}: {count}\n"

    conteo_textbox.config(state=tk.NORMAL)
    conteo_textbox.delete('1.0', tk.END)
    conteo_textbox.insert(tk.END, conteo_text)
    conteo_textbox.config(state=tk.DISABLED)

ventana = tk.Tk()
ventana.title("Analizador Léxico")

etiqueta = tk.Label(ventana, text="Ingrese la expresión:")
entrada = scrolledtext.ScrolledText(ventana, height=10, width=40) 
analizar_button = tk.Button(ventana, text="Analizar", command=analizar_button_click)

resultado_textbox = scrolledtext.ScrolledText(ventana, height=10, width=40)
resultado_textbox.config(state=tk.DISABLED)

conteo_textbox = scrolledtext.ScrolledText(ventana, height=10, width=20)
conteo_textbox.config(state=tk.DISABLED)

etiqueta.pack(pady=10)
entrada.pack(pady=10)
analizar_button.pack(pady=10)
resultado_textbox.pack(side='right', padx=10, pady=10, fill='both', expand=True)
conteo_textbox.pack(side='right', padx=10, pady=10, fill='both', expand=True)

ventana.mainloop()
