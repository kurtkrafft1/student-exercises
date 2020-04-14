from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

###### Exercises
flexbox = Exercise('Flex-box Froggy', "CSS")
itinerary = Exercise('Nashville Itinerary', "Javascript")
nutshell = Exercise('First Nutshell', "Javascript")
cars = Exercise('Cars', "Python")
python_tutorial = Exercise('Python Tutorial', 'Python')
react_project = Exercise('React Project', 'Javascript')
c_sharp_gold = Exercise('C# Gold', 'C#')
chicken_monkey = Exercise('Chicken_Monkey', 'Python')
css_grid = Exercise('CSS Grid', 'CSS')
UI_test = Exercise('UI_Test', 'CSS')
word_doc = Exercise('Word Document', 'Microsoft Word')
puzzles = Exercise('Puzzles', 'books')

##### Cohorts

cohort_37 = Cohort("Day Cohort 37", [], [] )
cohort_38 = Cohort("Day Cohort 38", [], [] )
cohort_39 = Cohort("Night Cohort 39", [], [] )

######Students

jim = Student('Jim', 'Halpert', 'lil_jimmy', 38, python_tutorial,react_project)
dwight = Student('Dwight', "Shrute", 'beets_FTW', 37, c_sharp_gold, chicken_monkey)
pam = Student('Pam', 'Beasley', 'white_shoes_4Eva', 39, css_grid, UI_test)
creed = Student('Creed', "Bratton", 'www.creedthoughts.com/gov', 38, word_doc, puzzles)


###### Instructors

andy= Instructor('Andy', 'Collins', 'handy_andy_4', cohort_38, 'yo-yos')
bryan = Instructor('Bryan', 'Nielsen', 'B-Nee-Baby', cohort_39, 'betrayal')
michael = Instructor('Michael', 'Scott', '80085_lol', cohort_37, 'being the best damn boss ever')

andy.assign_exercise(flexbox, jim)
andy.assign_exercise(itinerary, jim)

andy.assign_exercise(flexbox, creed)
andy.assign_exercise(cars, creed)

bryan.assign_exercise(nutshell, pam)
bryan.assign_exercise(itinerary, pam)

michael.assign_exercise(cars, dwight)
michael.assign_exercise(nutshell, dwight)


#########Challenge
students = [jim, dwight, pam, creed]

for student in students:
    exercises = student.exercises
    last_one = exercises[-1]
    exercises.pop(-1)
    exercise_names = list()
    for exercise in exercises:
        exercise_names.append(exercise.name)

    joint = ", ".join(exercise_names)
    print(f"{student.first_name} is currently working on {joint} and {last_one.name} exercises")


    





