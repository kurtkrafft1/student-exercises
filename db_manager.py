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
    
    def get_student_exercise_dictionary(self, version):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
            e.exercise_id exercise_id,
            e.name,
            e.language,
            s.first_name, 
            s.last_name,
            i.first_name as instructor_first,
            i.last_name instructor_last
            from Exercise e 
            join Student_Exercises se on se.exercise_Id = e.exercise_id
            join Student s on s.id = se.Student_Id
            join Instructor i on i.instructor_id = se.instructorId
            """)

            all_student_exercise_data = db_cursor.fetchall()
            exercises = dict()

            for data in all_student_exercise_data:
                exercise_id = data[0]
                exercise_name = data[1]
                exercise_language = data[2]
                instructor_name = f"{data[5]} {data[6]}"
                student_name = f"{data[3]} {data[4]}"

                if version == "all":
                    if exercise_name not in exercises:
                        exercises[exercise_name] = {"students": [student_name], "instructors": [instructor_name]}
                    else:
                        exercises[exercise_name]["students"].append(student_name)
                        if instructor_name not in exercises[exercise_name]["instructors"]:
                            exercises[exercise_name]["instructors"].append(instructor_name)
                            
                if version == "student":
                    if student_name not in exercises:
                        exercises[student_name] = [exercise_name]
                    else:
                        exercises[student_name].append(exercise_name)

                if  version == "instructor":
                    if instructor_name not in exercises:
                        exercises[instructor_name] = [exercise_name]
                    else:
                        exercises[instructor_name].append(exercise_name)
                if version == "both" :
                    if exercise_name not in exercises:
                        exercises[exercise_name] = [(instructor_name, student_name)]
                    else:
                        exercises[exercise_name].append((instructor_name, student_name))
            
            return exercises
    def get_students_cohorts_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
            c.name,
            s.first_name as student_fn,
            s.last_name as student_ln,
            i.first_name as instruct_fn,
            i.last_name as instruct_ln
            from Student s 
            join Cohort c on c.cohort_id = s.cohort_id
            join Instructor i on i.cohort_id = c.cohort_id
            """)

            all_data = db_cursor.fetchall()
            cohort_dict = dict()

            for data in all_data:
                cohort_name = data[0]
                student_name = f"{data[1]} {data[2]}"
                instructor_name = f"{data[3]} {data[4]}"

                if cohort_name not in cohort_dict:
                    cohort_dict[cohort_name] = {"students" : [student_name], "instructors" : [instructor_name]}
                else:
                    cohort_dict[cohort_name]["students"].append(student_name)
                    cohort_dict[cohort_name]["instructors"].append(instructor_name)
                    
            return cohort_dict

