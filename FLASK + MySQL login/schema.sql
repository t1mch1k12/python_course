CREATE DATABASE IF NOT EXISTS flask_auth CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE flask_auth;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(64) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL
);
-- Пароль добавляется через create_user.py в виде безопасного хеша.
