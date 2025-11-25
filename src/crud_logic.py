from db import conectar
from validaciones import validar_pelicula
from logging_config import log_transacciones, log_errores

# INSERTAR
def insertar_pelicula_logic(titulo, director, año, genero, calificacion):
    error = validar_pelicula(titulo, año, calificacion)
    if error:
        return False, error
    try:
        conexion = conectar()
        if conexion is None:
            return False, "No hay conexión con la base de datos."

        cursor = conexion.cursor()
        sql = """
        INSERT INTO peliculas (titulo, director, año, genero, calificacion) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (titulo, director, año, genero, calificacion))
        conexion.commit()
        log_transacciones.info(f"Insertada película: {titulo}")
        return True, "Película insertada correctamente."
    except Exception as e:
        log_errores.error(f"Error al insertar: {e}")
        return False, "Ocurrió un error al insertar."
    finally:
        if conexion:
            conexion.close()

# MOSTRAR
def mostrar_peliculas_logic():
    try:
        conexion = conectar()
        if conexion is None:
            return []
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        datos = cursor.fetchall()
        log_transacciones.info("Se consultaron las películas")
        return list(datos)
    except Exception as e:
        log_errores.error(f"Error al mostrar: {e}")
        return []
    finally:
        if conexion:
            conexion.close()

# ACTUALIZAR
def actualizar_pelicula_logic(id_pelicula, titulo, director, año, genero, calificacion):
    error = validar_pelicula(titulo, año, calificacion)
    if error:
        return False, error
    if not id_pelicula or not id_pelicula.isdigit():
        return False, "Debe proporcionar un ID válido."
    try:
        conexion = conectar()
        if conexion is None:
            return False, "No hay conexión con la base de datos."
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE id=%s", (id_pelicula,))
        if cursor.fetchone() is None:
            return False, "No existe una película con ese ID."
        sql = """
        UPDATE peliculas
        SET titulo=%s, director=%s, año=%s, genero=%s, calificacion=%s
        WHERE id=%s
        """
        cursor.execute(sql, (titulo, director, año, genero, calificacion, id_pelicula))
        conexion.commit()
        log_transacciones.info(f"Actualizada película ID {id_pelicula}")
        return True, "Película actualizada correctamente."
    except Exception as e:
        log_errores.error(f"Error al actualizar: {e}")
        return False, "Ocurrió un error al actualizar."
    finally:
        if conexion:
            conexion.close()

# ELIMINAR
def eliminar_pelicula_logic(id_pelicula):
    if not id_pelicula or not id_pelicula.isdigit():
        return False, "Debe proporcionar un ID válido."
    try:
        conexion = conectar()
        if conexion is None:
            return False, "No hay conexión con la base de datos."
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE id=%s", (id_pelicula,))
        if cursor.fetchone() is None:
            return False, "No existe una película con ese ID."
        cursor.execute("DELETE FROM peliculas WHERE id=%s", (id_pelicula,))
        conexion.commit()
        log_transacciones.info(f"Eliminada película ID {id_pelicula}")
        return True, "Película eliminada correctamente."
    except Exception as e:
        log_errores.error(f"Error al eliminar: {e}")
        return False, "Ocurrió un error al eliminar."
    finally:
        if conexion:
            conexion.close()
