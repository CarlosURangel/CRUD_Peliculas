# tests/test_crud.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.crud_logic import (
    insertar_pelicula_logic,
    mostrar_peliculas_logic,
    actualizar_pelicula_logic,
    eliminar_pelicula_logic 
)



# Datos de prueba
PELICULA_INSERTAR = {
    "titulo": "TestPelícula",
    "director": "TestDirector",
    "año": "2022",
    "genero": "Acción",
    "calificacion": "8.5",
}

PELICULA_ACTUALIZAR = {
    "titulo": "TestPelículaActualizada",
    "director": "DirectorActualizado",
    "año": "2023",
    "genero": "Comedia",
    "calificacion": "9",
}

def test_insertar_pelicula():
    ok, msg = insertar_pelicula_logic(**PELICULA_INSERTAR)
    assert ok, f"No se pudo insertar la película: {msg}"

def test_mostrar_peliculas():
    peliculas = mostrar_peliculas_logic()
    assert isinstance(peliculas, list)
    assert any(p[1] == PELICULA_INSERTAR["titulo"] for p in peliculas)

def test_actualizar_pelicula():
    peliculas = mostrar_peliculas_logic()
    assert peliculas, "No hay películas para actualizar"
    ultima_id = str(peliculas[-1][0])
    ok, msg = actualizar_pelicula_logic(ultima_id, **PELICULA_ACTUALIZAR)
    assert ok, f"No se pudo actualizar la película: {msg}"
    peliculas = mostrar_peliculas_logic()
    assert any(p[1] == PELICULA_ACTUALIZAR["titulo"] for p in peliculas)

def test_actualizar_id_inexistente():
    ok, msg = actualizar_pelicula_logic("999999", **PELICULA_ACTUALIZAR)
    assert not ok
    assert msg == "No existe una película con ese ID."

def test_eliminar_pelicula():
    peliculas = mostrar_peliculas_logic()
    assert peliculas, "No hay películas para eliminar"
    ultima_id = str(peliculas[-1][0])
    ok, msg = eliminar_pelicula_logic(ultima_id)
    assert ok, f"No se pudo eliminar la película: {msg}"
    peliculas = mostrar_peliculas_logic()
    assert all(p[0] != int(ultima_id) for p in peliculas)
