CREATE DATABASE IF NOT EXISTS gestion_inmuebles
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;


CREATE USER IF NOT EXISTS 'usr_inmuebles'@'%' IDENTIFIED BY 'Inmuebles2026!';


GRANT ALL PRIVILEGES ON gestion_inmuebles.* TO 'usr_inmuebles'@'%';


FLUSH PRIVILEGES;
