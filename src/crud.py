"""
Archivo donde se declaran las funciones para el CRUD
"""

from tkinter import messagebox
from db import conectar
from logging_config import log_transacciones, log_errores
from validaciones import validar_pelicula

def insertar_pelicula(titulo, director, año, genero, calificacion):
    """
    Función para insertar película
    """
    error = validar_pelicula(titulo, año, calificacion)
    if error:
        messagebox.showerror("Error", error)
        return
    try:
        conexion = conectar()
        if conexion is None:
            messagebox.showerror("Error", "No hay conexión con la base de datos.")
            return

        cursor = conexion.cursor()
        sql = """
        INSERT INTO peliculas (titulo, director, año, genero, calificacion) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (titulo, director, año, genero, calificacion))
        conexion.commit()
        log_transacciones.info(f"Insertada película: {titulo}")
        messagebox.showinfo("Éxito", "Película insertada correctamente.")

    except Exception as e:
        log_errores.error(f"Error al insertar: {e}")
        messagebox.showerror("Error", "Ocurrió un error al insertar.")

    finally:
        if conexion:
            conexion.close()

def mostrar_peliculas():
    """
    Función para mostrar películas
    """
    try:
        conexion = conectar()
        if conexion is None:
            messagebox.showerror("Error", "No hay conexión con la base de datos.")
            return []

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        datos = cursor.fetchall()
        log_transacciones.info("Se consultaron las películas")
        return datos

    except Exception as e:
        log_errores.error(f"Error al mostrar: {e}")
        messagebox.showerror("Error", "Ocurrió un error al consultar.")
        return []

    finally:
        if conexion:
            conexion.close()
