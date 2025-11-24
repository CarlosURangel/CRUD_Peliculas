"""
Validaciones de formato en los campos de texto de la app
"""

def validar_pelicula(titulo, año, calificacion):
    """
    Verifica que el título, año y calificación tengan el formato correcto
    """
    if not titulo:
        return "El título es obligatorio."
    if año and not año.isdigit() :
        return "El año debe ser un número."
    año_int = int(año)
    if año_int < 1900 or año_int > 2026:
        return "El año debe estar entre 1900 y 2026."
    if calificacion:
        try:
            c = float(calificacion)
            if c < 0 or c > 10:
                return "La calificación debe estar entre 0 y 10."
        except Exception:
            return "La calificación debe ser numérica."
    return None
