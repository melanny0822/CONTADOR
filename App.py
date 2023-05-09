import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import string


class ContadorPalabras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Contador de Palabras")

        # Crear widgets
        self.label = tk.Label(self.ventana, text="Ingresa o pega el texto:", bg="black", fg="white")
        self.label.pack()

        self.text = tk.Text(self.ventana, height=20, width=40)
        self.text.pack()

        self.count_button = tk.Button(self.ventana, text="Contar Palabras", command=self.contar_palabras, bg="black", fg="white")
        self.count_button.pack(side=tk.LEFT, padx=5)

        self.exportar_button = tk.Button(self.ventana, text="Exportar a Archivo", command=self.exportar_palabras, bg="black", fg="white")
        self.exportar_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.ventana, text="Limpiar", command=self.Limpiar_texto, bg="black", fg="white")
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.ventana, text="Salir", command=self.Salir, bg="black", fg="white")
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Inicializar contador de palabras
        self.Palabras_Contadas = {}

    def contar_palabras(self):
        # Obtener el texto del cuadro de texto
        text = self.text.get("1.0", tk.END)
        # Validar si se ha ingresado texto

        if text.isspace():
            messagebox.showerror("Error", "Por favor ingresa o pega un texto antes de contar las palabras.")
            return

        # Limpiar signos de puntuación
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Dividir el texto en palabras
        Palabras = text.split()

        # Contar las palabras
        for Palabra in Palabras:
            if Palabra in self.Palabras_Contadas:
                self.Palabras_Contadas[Palabra] += 1
            else:
                self.Palabras_Contadas[Palabra] = 1

        # Mostrar los resultados en una ventana emergente
        messagebox.showinfo("Resultado", f"Frecuencia de Palabras:\n{self.Palabras_Contadas}")

    def exportar_palabras(self):
        # Obtener el directorio de archivo de texto
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        # Guardar las palabras contadas en un archivo de texto
        with open(file_path, "w") as file:
            for palabra, count in self.Palabras_Contadas.items():
                file.write(f"{palabra}: {count}\n")

        # Mostrar un mensaje de éxito en una ventana emergente
        messagebox.showinfo("Exportación Exitosa",
                            f"Las palabras contadas se han exportado correctamente")

        # Limpiar el contenido de la ventana
        self.Limpiar_texto()

    def Limpiar_texto(self):
        # Limpiar el contenido del cuadro de texto
        self.text.delete("1.0", tk.END)

    def Salir(self):
        # Cerrar la ventana de tkinter
        self.ventana.destroy()


# Crear la ventana de la GUI
ventana = tk.Tk()
ventana.geometry("400x500")
ventana.config(bg="AQUA")

# Crear una instancia del contador de palabras
word_counter = ContadorPalabras(ventana)

# Iniciar el ciclo de eventos de la GUI
ventana.mainloop()
