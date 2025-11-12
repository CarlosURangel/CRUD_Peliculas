import customtkinter as ctk
from tkinter import messagebox

# ----------------- FUNCIONES CRUD (a implementar paso a paso) -----------------
def insertar_pelicula(titulo, director, anio, genero, calificacion):
    messagebox.showinfo("Insertar", f"Insertar película: {titulo}, {director}, {anio}, {genero}, {calificacion}")

def mostrar_peliculas():
    salida_text.delete("1.0", ctk.END)
    peliculas = [
        (1, "Inception", "Christopher Nolan", 2010, "Ciencia Ficción", 9.0),
        (2, "Parasite", "Bong Joon-ho", 2019, "Thriller", 8.6),
        (3, "Interstellar", "Christopher Nolan", 2014, "Ciencia Ficción", 8.5)
    ]
    for p in peliculas:
        salida_text.insert(ctk.END, f"ID: {p[0]} | Título: {p[1]} | Director: {p[2]} | Año: {p[3]} | Género: {p[4]} | Calificación: {p[5]}\n")

def actualizar_pelicula(id_pelicula, titulo, director, anio, genero, calificacion):
    messagebox.showinfo("Actualizar", f"Actualizar película {id_pelicula} con nuevos datos.")

def eliminar_pelicula(id_pelicula):
    messagebox.showinfo("Eliminar", f"Eliminar película con ID: {id_pelicula}")

# --------------------------- INTERFAZ CON CUSTOMTKINTER ---------------------------
if __name__ == "__main__":

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    ventana = ctk.CTk()
    ventana.title("Gestión de Películas - CRUD")
    ventana.geometry("420x550")

    # Entradas de datos
    ctk.CTkLabel(ventana, text="ID Película:").pack(pady=5)
    entry_id = ctk.CTkEntry(ventana, width=200)
    entry_id.pack()

    ctk.CTkLabel(ventana, text="Título:").pack(pady=5)
    entry_titulo = ctk.CTkEntry(ventana, width=200)
    entry_titulo.pack()

    ctk.CTkLabel(ventana, text="Director:").pack(pady=5)
    entry_director = ctk.CTkEntry(ventana, width=200)
    entry_director.pack()

    ctk.CTkLabel(ventana, text="Año:").pack(pady=5)
    entry_anio = ctk.CTkEntry(ventana, width=200)
    entry_anio.pack()

    ctk.CTkLabel(ventana, text="Género:").pack(pady=5)
    entry_genero = ctk.CTkEntry(ventana, width=200)
    entry_genero.pack()

    ctk.CTkLabel(ventana, text="Calificación (0-10):").pack(pady=5)
    entry_calificacion = ctk.CTkEntry(ventana, width=200)
    entry_calificacion.pack()

    # Botones
    frame_botones = ctk.CTkFrame(ventana)
    frame_botones.pack(pady=10)

    btn_insertar = ctk.CTkButton(
        frame_botones,
        text="Insertar",
        command=lambda: insertar_pelicula(
            entry_titulo.get(), entry_director.get(), entry_anio.get(), entry_genero.get(), entry_calificacion.get()
        )
    )
    btn_insertar.grid(row=0, column=0, padx=5, pady=5)

    btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar", command=mostrar_peliculas)
    btn_mostrar.grid(row=0, column=1, padx=5, pady=5)

    btn_actualizar = ctk.CTkButton(
        frame_botones,
        text="Actualizar",
        command=lambda: actualizar_pelicula(
            entry_id.get(), entry_titulo.get(), entry_director.get(), entry_anio.get(), entry_genero.get(), entry_calificacion.get()
        )
    )
    btn_actualizar.grid(row=1, column=0, padx=5, pady=5)

    btn_eliminar = ctk.CTkButton(
        frame_botones,
        text="Eliminar",
        fg_color="#D9534F",
        hover_color="#C9302C",
        command=lambda: eliminar_pelicula(entry_id.get())
    )
    btn_eliminar.grid(row=1, column=1, padx=5, pady=5)

    btn_salir = ctk.CTkButton(frame_botones, text="Salir", command=ventana.destroy)
    btn_salir.grid(row=2, column=1, padx=5, pady=5)

    # Área de salida
    salida_text = ctk.CTkTextbox(ventana, width=360, height=120)
    salida_text.pack(pady=10)

    ventana.mainloop()
