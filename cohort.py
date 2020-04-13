class Cohort:

    def __init__(self, name, students, instructors):
        self.name = name
        self.students = students
        self.instructors = instructors

    def add_students(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)
        
    def remove_instructor (self, instructor):
        self.instructors.remove(instructor)