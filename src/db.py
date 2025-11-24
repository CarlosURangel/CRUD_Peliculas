"""
Archivo para la conexión a la base de datos
"""
import pymysql
from logging_config import log_transacciones, log_errores

def conectar():
    """
    Crea la conexión con la base de datos
    """
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="peliculas_db",
            port=3306
        )
        log_transacciones.info("Conexión establecida con la base de datos")
        return conexion
    except Exception as e:
        log_errores.error(f"Error al conectar a la base de datos: {e}")
        return None
