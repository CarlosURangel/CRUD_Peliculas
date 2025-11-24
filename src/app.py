import customtkinter as ctk
from tkinter import messagebox
from crud import insertar_pelicula, mostrar_peliculas
from logging_config import log_transacciones, log_errores



def accion_insertar():
    insertar_pelicula(
        entry_titulo.get(),
        entry_director.get(),
        entry_año.get(),
        entry_genero.get(),
        entry_calificacion.get()
    )

def accion_mostrar():
    salida_text.delete("1.0", "end")
    peliculas = mostrar_peliculas()

    if not peliculas:
        salida_text.insert("end", "No hay películas registradas.\n")
        return

    for p in peliculas:
        salida_text.insert("end", f"ID: {p[0]} | Título: {p[1]} | Director: {p[2]} | Año: {p[3]} | Género: {p[4]} | Calificación: {p[5]}\n")


def actualizar_pelicula(id_pelicula, titulo, director, año, genero, calificacion):
    messagebox.showinfo("Actualizar", f"Actualizar película {id_pelicula} con nuevos datos.")

def eliminar_pelicula(id_pelicula):
    messagebox.showinfo("Eliminar", f"Eliminar película con ID: {id_pelicula}")

if __name__ == "__main__":

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    ventana = ctk.CTk()
    ventana.title("Gestión de Películas")
    ventana.geometry("700x500")

    frame_campos = ctk.CTkFrame(ventana)
    frame_campos.pack(pady=10)

    ctk.CTkLabel(frame_campos, text="ID Película:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_id = ctk.CTkEntry(frame_campos, width=180)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(frame_campos, text="Título:").grid(row=0, column=2, padx=10, pady=5, sticky="e")
    entry_titulo = ctk.CTkEntry(frame_campos, width=180)
    entry_titulo.grid(row=0, column=3, padx=10, pady=5)

    ctk.CTkLabel(frame_campos, text="Director:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_director = ctk.CTkEntry(frame_campos, width=180)
    entry_director.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(frame_campos, text="Año:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
    entry_año = ctk.CTkEntry(frame_campos, width=180)
    entry_año.grid(row=1, column=3, padx=10, pady=5)

    ctk.CTkLabel(frame_campos, text="Género:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_genero = ctk.CTkEntry(frame_campos, width=180)
    entry_genero.grid(row=2, column=1, padx=10, pady=5)

    ctk.CTkLabel(frame_campos, text="Calificación (0-10):").grid(row=2, column=2, padx=10, pady=5, sticky="e")
    entry_calificacion = ctk.CTkEntry(frame_campos, width=180)
    entry_calificacion.grid(row=2, column=3, padx=10, pady=5)

    frame_botones = ctk.CTkFrame(ventana)
    frame_botones.pack(pady=10)

    btn_insertar = ctk.CTkButton(frame_botones, text="Insertar", width=100, command=accion_insertar)
    btn_insertar.grid(row=0, column=0, padx=5, pady=5)

    btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar", width=100, command=accion_mostrar)
    btn_mostrar.grid(row=0, column=1, padx=5, pady=5)

    btn_actualizar = ctk.CTkButton(frame_botones, text="Actualizar", width=100, command=lambda: actualizar_pelicula(entry_id.get(), entry_titulo.get(), entry_director.get(), entry_año.get(), entry_genero.get(), entry_calificacion.get()))
    btn_actualizar.grid(row=0, column=2, padx=5, pady=5)

    btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar", width=100, fg_color="#D9534F", hover_color="#C9302C", command=lambda: eliminar_pelicula(entry_id.get()))
    btn_eliminar.grid(row=0, column=3, padx=5, pady=5)

    salida_text = ctk.CTkTextbox(ventana, width=600, height=180)
    salida_text.pack(pady=10)

    btn_salir = ctk.CTkButton(ventana, text="Salir", command=ventana.destroy)
    btn_salir.pack(pady=10)

    ventana.mainloop()
