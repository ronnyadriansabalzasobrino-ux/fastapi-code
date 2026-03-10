
CREATE TABLE Programs (
    id_program SERIAL PRIMARY KEY,
    name_program VARCHAR(100) NOT NULL,
    faculty VARCHAR(100) NOT NULL,
    level VARCHAR(50) NOT NULL
);


CREATE TABLE Semesters (
    id_semester SERIAL PRIMARY KEY,
    number_semesters INT NOT NULL CHECK (number_semesters > 0),
    description VARCHAR(100)
);


CREATE TABLE Periods (
    id_period SERIAL PRIMARY KEY,
    period_code VARCHAR(10) UNIQUE NOT NULL,
    start_date DATE,
    end_date DATE
);


CREATE TABLE Students (
    id_student SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    number_id VARCHAR(20) UNIQUE NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    id_program INT REFERENCES programs(id_program),
    id_semester INT REFERENCES semesters(id_semester),
    registration_date DATE DEFAULT CURRENT_DATE,
    state VARCHAR(20) DEFAULT 'asset'
        CHECK (state IN ('asset','inactive'))
);


CREATE TABLE Teacher (
    id_teaching SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    number_id VARCHAR(20) UNIQUE NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    speciality VARCHAR(100)
);


CREATE TABLE Users (
    id_user SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    post VARCHAR(100) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    rol VARCHAR(50) NOT NULL
);


CREATE TABLE Subject (
    id_subject SERIAL PRIMARY KEY,
    name_subject VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0),
    id_program INT REFERENCES programs(id_program)
);


CREATE TABLE Teacher_subject(
    id_teacher_subject SERIAL PRIMARY KEY,
    id_teaching INT REFERENCES teacher(id_teaching) ON DELETE CASCADE,
    id_subject INT REFERENCES subject(id_subject) ON DELETE CASCADE,
    periodo_academico VARCHAR(20) NOT NULL,
    id_period INT REFERENCES periods(id_period)
);


CREATE TABLE Student_subject (
    id_student_subject SERIAL PRIMARY KEY,
    id_student INT REFERENCES students(id_student) ON DELETE CASCADE,
    id_subject INT REFERENCES subject(id_subject) ON DELETE CASCADE,
    academic_period VARCHAR(20) NOT NULL,
    state VARCHAR(20) DEFAULT 'studying'
        CHECK (state IN ('studying','approved','reprobate')),
    id_period INT REFERENCES periods(id_period)
);


CREATE TABLE Note (
    id_note SERIAL PRIMARY KEY,
    id_student_subject INT REFERENCES student_subject(id_student_subject) ON DELETE CASCADE,
    evaluation_type VARCHAR(50) NOT NULL,
    percentage NUMERIC(5,2) CHECK (percentage >= 0 AND percentage <= 100),
    qualification NUMERIC(3,2) CHECK (qualification >= 0 AND qualification <= 5),
    registration_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Assists (
    id_assists SERIAL PRIMARY KEY,
    id_student_subject INT REFERENCES student_subject(id_student_subject) ON DELETE CASCADE,
    date DATE NOT NULL,
    state VARCHAR(20)
        CHECK (state IN ('attended','lack','excuse'))
);


CREATE TABLE Alerts (
    id_alert SERIAL PRIMARY KEY,
    id_student INT REFERENCES students(id_student) ON DELETE CASCADE,
    tipo_alert VARCHAR(50) NOT NULL,
    description TEXT,
    generation_date DATE DEFAULT CURRENT_DATE,
    risk_level VARCHAR(20)
        CHECK (risk_level IN ('low','medium','high')),
    state VARCHAR(20) DEFAULT 'active'
        CHECK (state IN ('active','closed')),
    id_period INT REFERENCES periods(id_period)
);


CREATE TABLE Followups (
    id_followup SERIAL PRIMARY KEY,
    id_alert INT REFERENCES alerts(id_alert) ON DELETE CASCADE,
    id_teaching INT REFERENCES teacher(id_teaching),
    observation TEXT NOT NULL,
    followup_date DATE DEFAULT CURRENT_DATE,
    action_taken TEXT
);