import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Change this
    database="student_db"
)
cursor = conn.cursor()

def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")

    try:
        cursor.execute("INSERT INTO students (roll_no, name, age, gender, course) VALUES (%s, %s, %s, %s, %s)",
                       (roll_no, name, age, gender, course))
        conn.commit()
        print("Student added successfully!\n")
    except Exception as e:
        print("Error:", e)

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nAll Students:")
    for row in rows:
        print(row)
    print()

def update_student():
    roll_no = int(input("Enter Roll Number to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    gender = input("Enter New Gender: ")
    course = input("Enter New Course: ")

    cursor.execute("UPDATE students SET name=%s, age=%s, gender=%s, course=%s WHERE roll_no=%s",
                   (name, age, gender, course, roll_no))
    conn.commit()
    print("Student updated successfully!\n")

def delete_student():
    roll_no = int(input("Enter Roll Number to Delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_no,))
    conn.commit()
    print("Student deleted successfully!\n")

def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.\n")

main()
cursor.close()
conn.close()
