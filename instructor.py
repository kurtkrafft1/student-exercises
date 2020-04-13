class Instructor:

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty
    
    def assign_exercise(self, exercise, student):
        student.exercises.append(exercise)
        print(f"looks like {self.first_name} has assigned {student.first_name} the {exercise.name} exercise")