from logger import logger
from database import conn

def insert_name():
    name = input("Enter student name: ")
    phone = input("Enter student phone (max 10 chars): ")
    city = input("Enter student city: ")
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO Student (Name, Phone, City) VALUES (%s, %s, %s)",
                (name, phone, city)
            )
        conn.commit()
        logger.info(f"Successfully inserted student: {name}")
        print(f"Student '{name}' added successfully!")
    except Exception as e:
        conn.rollback()
        logger.error(f"Failed to insert student: {e}")
        print(f"Error: {e}")

def retrieve_data():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT Student_id, Name, Phone, City FROM Student;")
            students = cur.fetchall()
            
            print("\n--- Student Details ---")
            for s in students:
                print(f"ID: {s[0]} | Name: {s[1]} | Phone: {s[2]} | City: {s[3]}")
            print("-----------------------\n")
            logger.info("Retrieved student records.")
    except Exception as e:
        logger.error(f"Failed to retrieve students: {e}")
        print(f"Error: {e}")

def insert_course():
    course_name = input("Enter course name: ")
    duration = input("Enter course duration: ")
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO Course (Course_name, Duration) VALUES (%s, %s)",
                (course_name, duration)
            )
        conn.commit()
        logger.info(f"Successfully inserted course: {course_name}")
        print(f"Course '{course_name}' added successfully!")
    except Exception as e:
        conn.rollback()
        logger.error(f"Failed to insert course: {e}")
        print(f"Error: {e}")

def select_course():
    course_id = input("Enter Course ID to view enrolled students: ")
    try:
        with conn.cursor() as cur:
            query = """
                SELECT s.Student_id, s.Name, c.Course_name, e.Start_date
                FROM Student s
                JOIN Enrollment e ON s.Student_id = e.Student_id
                JOIN Course c ON e.Course_id = c.Course_id
                WHERE c.Course_id = %s;
            """
            cur.execute(query, (course_id,))
            records = cur.fetchall()
            
            print(f"\n--- Students Enrolled in Course ID: {course_id} ---")
            if not records:
                print("No students found for this course.")
            else:
                for row in records:
                    print(f"Student ID: {row[0]} | Name: {row[1]} | Course: {row[2]} | Enrolled: {row[3]}")
            print("------------------------------------------------\n")
            logger.info(f"Retrieved enrolled students for course ID: {course_id}")
    except Exception as e:
        logger.error(f"Failed to retrieve enrolled students: {e}")
        print(f"Error: {e}")

def enroll_student():
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO Enrollment (Student_id, Course_id) VALUES (%s, %s)",
                (student_id, course_id)
            )
        conn.commit()
        logger.info(f"Successfully enrolled student {student_id} in course {course_id}")
        print("Student enrolled successfully!")
    except Exception as e:
        conn.rollback()
        logger.error(f"Failed to enroll student: {e}")
        print(f"Error: {e}")

while True:
    print("\n=== Menu ===")
    print("1 -> Enter student details")
    print("2 -> Get student details")
    print("3 -> Enter course details")
    print("4 -> Get enrolled students in the course")
    print("5 -> Enroll a student in a course")
    print("6 -> Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        insert_name()
    elif choice == "2":
        retrieve_data()
    elif choice == "3":
        insert_course()
    elif choice == "4":
        select_course()
    elif choice == "5":
        enroll_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
