class Cohort:

    def __init__(self,cohort_id, name):
        self.cohort_id = cohort_id
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_students(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)
        
    def remove_instructor (self, instructor):
        self.instructors.remove(instructor)
    