CREATE DATABASE IF NOT EXISTS trigger_lesson;
USE trigger_lesson;

-- Таблица с основными данными
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Таблица-журнал для действий AFTER INSERT
CREATE TABLE IF NOT EXISTS users_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Удаляем триггеры, если скрипт запускается повторно
DROP TRIGGER IF EXISTS trg_users_before_insert;
DROP TRIGGER IF EXISTS trg_users_after_insert;

DELIMITER $$

-- 1. BEFORE INSERT: нормализация данных перед сохранением
CREATE TRIGGER trg_users_before_insert
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    SET NEW.name = TRIM(NEW.name);
    SET NEW.email = LOWER(TRIM(NEW.email));
END$$

-- 2. AFTER INSERT: запись добавленного пользователя в журнал
CREATE TRIGGER trg_users_after_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO users_log (user_id, user_name, user_email)
    VALUES (NEW.id, NEW.name, NEW.email);
END$$

DELIMITER ;

-- Проверка работы триггеров
INSERT INTO users (name, email)
VALUES ('  Иван Иванов  ', '  IVAN@EXAMPLE.COM  ');

-- Результат: имя без лишних пробелов, e-mail в нижнем регистре
SELECT * FROM users;

-- В журнале должна появиться запись о добавленном пользователе
SELECT * FROM users_log;

-- Дополнительная проверка: список созданных триггеров
SHOW TRIGGERS;
