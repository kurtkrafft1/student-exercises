class Student:

    def __init__(self, first_name, last_name, slack_handle, cohort, *exercises):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises = list(exercises)
    
    def add_new_exercise(self, new_ex):
        self.exercises.append(new_ex)
    
    def complete_exercise(self, old_ex):
        self.exercises.remove(old_ex)
    
    
