import psycopg2

conn = psycopg2.connect(
    database="Student_record",
    user="postgres",
    password="Pratham@19",
    host="127.0.0.1",
    port="5432"
)

cursor = conn.cursor()