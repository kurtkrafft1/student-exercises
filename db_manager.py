import sqlite3
from student import Student
from exercise import Exercise
from instructor import Instructor
from cohort import Cohort

class Db_Manager():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/kurt/workspace/python/student_exercises/studentexercises.db"

    def student_data(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3],row[4], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.Name
            from Student s
            join Cohort c on s.cohort_id = c.cohort_id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()
            
            for student in all_students:
                print(student)

    def exercise_data(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exercise_id,
            e.name,
            e.language
            FROM Exercise e;
            """)
        
            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def exercise_data_by_language(self, language):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute(f"""
            SELECT e.exercise_id,
            e.name,
            e.language
            FROM Exercise e
            WHERE language like "{language}"
            """)
        
            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    
    def cohort_data(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0], row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.cohort_id,
            c.name
            FROM Cohort c;
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort.name)
        
    def instructor_data(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[5], row[6])
            db_cursor  = conn.cursor()

            db_cursor.execute("""
            SELECT 
            i.instructor_id,
            i.first_name,
            i.last_name,
            i.slack_handle,
            i.cohort_id,
            c.name,
            i.specialties
            FROM Instructor i 
            LEFT JOIN
            Cohort c on c.cohort_id = i.cohort_id
            ORDER BY i.cohort_id
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)
