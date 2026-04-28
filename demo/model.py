from database import cursor,conn
from logger import logger
logger.info("This is a test log message!")

def create_table():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS Student(
            Student_id SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Phone VARCHAR(10) UNIQUE NOT NULL,
            City VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Course(
            Course_id SERIAL PRIMARY KEY,
            Course_name VARCHAR(25) NOT NULL,
            Duration VARCHAR(25) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Enrollment(
            Student_id INT REFERENCES Student(Student_id),
            Course_id INT REFERENCES Course(Course_id),
            Start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(Student_id, Course_id)
        );
        """
    ]

    try: 
        for command in commands:
            cursor.execute(command)
        
        conn.commit()
        logger.info("All tables created and committed successfully.")

    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f"Database error: {e}")
    finally:
        cursor.close()


if __name__ == "__main__":
    create_table()