CREATE DATABASE event_db;
USE event_db;

-- Table for events
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date DATE,
    location VARCHAR(100)
);

-- Insert sample events
INSERT INTO events (name, date, location) 
VALUES 
('Tech Talk 2025', '2025-09-10', 'Auditorium A'),
('College Fest', '2025-10-01', 'Main Ground'),
('Webinar on AI', '2025-11-05', 'Online Zoom');

-- Table for registrations
CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

-- Table for admin
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);

-- Insert default admin
INSERT INTO admin (username, password) VALUES ('admin', 'admin123');
