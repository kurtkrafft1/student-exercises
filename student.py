from NSSperson import NSSperson

class Student(NSSperson):

    def __init__(self, first_name, last_name, slack_handle, cohort_id, cohort_name):
        super().__init__(first_name, last_name, slack_handle, cohort_id, cohort_name)
        self.exercises = list()
        
    
    def add_new_exercise(self, new_ex):
        self.exercises.append(new_ex)
    
    def complete_exercise(self, old_ex):
        self.exercises.remove(old_ex)


    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort_name}'
    
