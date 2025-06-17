# Student Management System (Python + MySQL)

This is a simple command-line Student Management System written in Python using MySQL as the backend database.

## Features
- Add Student
- View Students
- Update Student
- Delete Student

## Requirements
- Python 3
- mysql-connector-python
- MySQL Server

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the script:
```
python main.py
```

3. Before running, create the following MySQL database and table:
```sql
CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(100)
);
```
