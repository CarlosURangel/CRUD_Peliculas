CREATE DATABASE IF NOT EXISTS peliculas_db;
USE peliculas_db;

CREATE TABLE peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    director VARCHAR(100),
    año INT,
    genero VARCHAR(50),
    calificacion DECIMAL(3,1)
);

INSERT INTO peliculas (titulo, director, año, genero, calificacion)
VALUES 
("Una película de huevos", "Gabriel Riva Palacio Alatriste", 2006, "Animación", 6.7),
("Chicken Little", "Mark Dindal", 2005, "Animación", 5.7),
("Ratatouille", "Brad Bird", 2007, "Animación", 8.1);