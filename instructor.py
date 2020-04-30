from NSSperson import NSSperson

class Instructor(NSSperson):

    def __init__(self, first_name, last_name, slack_handle, cohort_id, cohort_name, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort_id, cohort_name)
        self.specialty = specialty
    
    def assign_exercise(self, exercise, student):
        student.exercises.append(exercise)
        print(f"looks like {self.first_name} has assigned {student.first_name} the {exercise.name} exercise")
    
    def __repr__(self):

        return f"{self.first_name} {self.last_name} is the instructor for {self.cohort_name} and their specialties are {self.specialty}"