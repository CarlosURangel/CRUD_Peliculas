"""
Interfaz de ejemplo para un CRUD de películas usando customtkinter.
Este archivo solo contiene la interfaz (widgets y callbacks de ejemplo).
Funciones de CRUD están como marcadores de posición (placeholders) para que
las implementes paso a paso.

Requisitos: pip install customtkinter

Ejecutar: python Interfaz_CRUD_Peliculas.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

APP_WIDTH = 900
APP_HEIGHT = 520

class MovieManagerUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de gestión de películas — Interfaz (CRUD)")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.minsize(800, 480)

        # Layout: izquierda = formulario y botones, derecha = lista/tablas
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._create_left_panel()
        self._create_right_panel()

    def _create_left_panel(self):
        left_frame = ctk.CTkFrame(self, width=320, corner_radius=8)
        left_frame.grid(row=0, column=0, padx=16, pady=16, sticky="nsew")
        left_frame.grid_rowconfigure(8, weight=1)

        title = ctk.CTkLabel(left_frame, text="Formulario de película", font=ctk.CTkFont(size=18, weight="bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(6, 12))

        # Campos del formulario
        self.entry_id = ctk.CTkEntry(left_frame, placeholder_text="ID (opcional)")
        self.entry_id.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        self.entry_title = ctk.CTkEntry(left_frame, placeholder_text="Título")
        self.entry_title.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        self.entry_director = ctk.CTkEntry(left_frame, placeholder_text="Director")
        self.entry_director.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        self.entry_year = ctk.CTkEntry(left_frame, placeholder_text="Año")
        self.entry_year.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        self.entry_genre = ctk.CTkEntry(left_frame, placeholder_text="Género")
        self.entry_genre.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        self.entry_rating = ctk.CTkEntry(left_frame, placeholder_text="Calificación (0-10)")
        self.entry_rating.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=6)

        # Botones de operación
        btn_create = ctk.CTkButton(left_frame, text="Crear", command=self.create_movie)
        btn_create.grid(row=7, column=0, sticky="ew", padx=(10,5), pady=12)

        btn_read = ctk.CTkButton(left_frame, text="Mostrar / Refrescar", command=self.read_movies)
        btn_read.grid(row=7, column=1, sticky="ew", padx=(5,10), pady=12)

        btn_update = ctk.CTkButton(left_frame, text="Actualizar", command=self.update_movie)
        btn_update.grid(row=8, column=0, sticky="ew", padx=(10,5), pady=(0,6))

        btn_delete = ctk.CTkButton(left_frame, text="Eliminar", fg_color="#D9534F", hover_color="#C9302C", command=self.delete_movie)
        btn_delete.grid(row=8, column=1, sticky="ew", padx=(5,10), pady=(0,6))

        btn_clear = ctk.CTkButton(left_frame, text="Limpiar campos", command=self.clear_form)
        btn_clear.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=(6,12))

        # Nota / ayuda
        help_text = ctk.CTkLabel(left_frame, text="Selecciona una fila en la lista para cargarla en el formulario.", wraplength=280, justify="left", fg_color=None)
        help_text.grid(row=10, column=0, columnspan=2, padx=10, pady=(6,0), sticky="w")

    def _create_right_panel(self):
        right_frame = ctk.CTkFrame(self, corner_radius=8)
        right_frame.grid(row=0, column=1, padx=(0,16), pady=16, sticky="nsew")
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(right_frame, text="Listado de películas", font=ctk.CTkFont(size=18, weight="bold"))
        title.grid(row=0, column=0, sticky="w", padx=12, pady=(6,12))

        # Treeview (tabla) para mostrar películas
        columns = ("id", "title", "director", "year", "genre", "rating")
        self.tree = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse")

        # Encabezados
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Título")
        self.tree.heading("director", text="Director")
        self.tree.heading("year", text="Año")
        self.tree.heading("genre", text="Género")
        self.tree.heading("rating", text="Calif.")

        # Anchuras
        self.tree.column("id", width=40, anchor="center")
        self.tree.column("title", width=220)
        self.tree.column("director", width=140)
        self.tree.column("year", width=60, anchor="center")
        self.tree.column("genre", width=100)
        self.tree.column("rating", width=60, anchor="center")

        # Scrollbar
        vsb = ttk.Scrollbar(right_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=1, column=0, sticky="nsew", padx=(12,0), pady=6)
        vsb.grid(row=1, column=1, sticky="ns", pady=6, padx=(4,12))

        # Bind selección
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Ejemplo: pequeñas herramientas bajo la tabla
        toolbar = ctk.CTkFrame(right_frame, corner_radius=6)
        toolbar.grid(row=2, column=0, columnspan=2, sticky="ew", padx=12, pady=(8,6))
        toolbar.grid_columnconfigure(0, weight=1)

        search_entry = ctk.CTkEntry(toolbar, placeholder_text="Buscar por título...", width=260)
        search_entry.grid(row=0, column=0, padx=6, pady=8, sticky="w")

        btn_search = ctk.CTkButton(toolbar, text="Buscar", width=90, command=lambda: messagebox.showinfo("Buscar", "Función de búsqueda (placeholder)"))
        btn_search.grid(row=0, column=1, padx=(6,12), pady=8)

    # ------------------------- Callbacks (placeholders) -------------------------
    def create_movie(self):
        # Capturar valores del formulario
        data = self._gather_form()
        # Aquí iría la lógica para insertar en la base de datos o lista
        print("Crear: ", data)
        messagebox.showinfo("Crear", "Función crear llamada. Implementa la inserción en tu backend.")

    def read_movies(self):
        # Aquí deberías obtener los datos reales desde tu fuente (db / archivo / API)
        # Por ahora mostraremos datos de ejemplo para que veas la interfaz funcionando.
        sample = [
            (1, "The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 9.3),
            (2, "Inception", "Christopher Nolan", 2010, "Ciencia ficción", 8.8),
            (3, "Parasite", "Bong Joon-ho", 2019, "Thriller", 8.6),
        ]
        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Insertar filas
        for item in sample:
            self.tree.insert("", tk.END, values=item)

    def update_movie(self):
        data = self._gather_form()
        print("Actualizar: ", data)
        messagebox.showinfo("Actualizar", "Función actualizar llamada. Implementa la actualización en tu backend.")

    def delete_movie(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Eliminar", "Selecciona una película en la lista para eliminarla.")
            return
        values = self.tree.item(selected[0], "values")
        print("Eliminar: ", values)
        messagebox.showinfo("Eliminar", "Función eliminar llamada. Implementa la eliminación en tu backend.")

    def clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_director.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_rating.delete(0, tk.END)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        # Asignar a formulario
        try:
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])

            self.entry_title.delete(0, tk.END)
            self.entry_title.insert(0, values[1])

            self.entry_director.delete(0, tk.END)
            self.entry_director.insert(0, values[2])

            self.entry_year.delete(0, tk.END)
            self.entry_year.insert(0, values[3])

            self.entry_genre.delete(0, tk.END)
            self.entry_genre.insert(0, values[4])

            self.entry_rating.delete(0, tk.END)
            self.entry_rating.insert(0, values[5])
        except Exception as e:
            print("Error cargando selección en formulario:", e)

    def _gather_form(self):
        return {
            "id": self.entry_id.get().strip(),
            "title": self.entry_title.get().strip(),
            "director": self.entry_director.get().strip(),
            "year": self.entry_year.get().strip(),
            "genre": self.entry_genre.get().strip(),
            "rating": self.entry_rating.get().strip(),
        }


if __name__ == "__main__":
    app = MovieManagerUI()
    # Cargar ejemplo inicial para que el usuario vea la tabla llena
    app.read_movies()
    app.mainloop()
