CREATE DATABASE student_db;
USE student_db;

CREATE TABLE student_performance (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    attendance_rate FLOAT,
    study_hours INT,
    previous_score INT,
    passed INT -- 1 for Pass, 0 for Fail
);

-- Insert some sample data
INSERT INTO student_performance (attendance_rate, study_hours, previous_score, passed) VALUES 
(0.95, 20, 88, 1),
(0.60, 5, 45, 0),
(0.85, 12, 70, 1),
(0.45, 2, 35, 0),
(0.75, 10, 60, 1);