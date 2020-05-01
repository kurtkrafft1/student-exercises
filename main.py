from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise
from db_manager import Db_Manager

###### Exercises

# flexbox = Exercise('Flex-box Froggy', "CSS")
# itinerary = Exercise('Nashville Itinerary', "Javascript")
# nutshell = Exercise('First Nutshell', "Javascript")
# cars = Exercise('Cars', "Python")
# python_tutorial = Exercise('Python Tutorial', 'Python')
# react_project = Exercise('React Project', 'Javascript')
# c_sharp_gold = Exercise('C# Gold', 'C#')
# chicken_monkey = Exercise('Chicken_Monkey', 'Python')
# css_grid = Exercise('CSS Grid', 'CSS')
# UI_test = Exercise('UI_Test', 'CSS')
# word_doc = Exercise('Word Document', 'Microsoft Word')
# puzzles = Exercise('Puzzles', 'books')

##### Cohorts

# cohort_37 = Cohort("Day Cohort 37", [], [] )
# cohort_38 = Cohort("Day Cohort 38", [], [] )
# cohort_39 = Cohort("Night Cohort 39", [], [] )

######Students

# jim = Student('Jim', 'Halpert', 'lil_jimmy', 38)
# dwight = Student('Dwight', "Shrute", 'beets_FTW', 37)
# pam = Student('Pam', 'Beasley', 'white_shoes_4Eva', 39)
# creed = Student('Creed', "Bratton", 'www.creedthoughts.com/gov', 38)


###### Instructors

# andy= Instructor('Andy', 'Collins', 'handy_andy_4', cohort_38, 'yo-yos')
# bryan = Instructor('Bryan', 'Nielsen', 'B-Nee-Baby', cohort_39, 'betrayal')
# michael = Instructor('Michael', 'Scott', '80085_lol', cohort_37, 'being the best damn boss ever')

# andy.assign_exercise(flexbox, jim)
# andy.assign_exercise(itinerary, jim)

# andy.assign_exercise(flexbox, creed)
# andy.assign_exercise(cars, creed)

# bryan.assign_exercise(nutshell, pam)
# bryan.assign_exercise(itinerary, pam)

# michael.assign_exercise(cars, dwight)
# michael.assign_exercise(nutshell, dwight)


#########Challenge
# students = [jim, dwight, pam, creed]

# for student in students:
#     exercises = student.exercises
#     last_one = exercises[-1]
#     exercises.pop(-1)
#     exercise_names = list()
#     for exercise in exercises:
#         exercise_names.append(exercise.name)

#     joint = ", ".join(exercise_names)
#     print(f"{student.first_name} is currently working on {joint} and {last_one.name} exercises")

data = Db_Manager()

print("----Students----")
data.student_data()
print("\n")

print("----Exercises----")
data.exercise_data()
print("\n")

print("----Cohorts----")
data.cohort_data()
print("\n")

langs = ["C#", "Python", "JavaScript"]
print("----By Language----")
for lang in langs:
    print(f"----{lang}----")
    data.exercise_data_by_language(lang)
print("\n")

print("----Instructors----")
data.instructor_data()
print("\n")

print("----Students, Instructors & Exercises----")
all_exercise_dict = data.get_student_exercise_dictionary("all")
for key, value in all_exercise_dict.items():
    print(f"    --{key}--")
    print(f"        --Students--")
    for student in value["students"]:
        print(f"            --{student}--")
    print(f"        --Assigned By--")
    for instructor in value["instructors"]:
        print(f"            --{instructor}--")
    print("\n\n")

print("\n")
student_exercise_dict = data.get_student_exercise_dictionary("student")
print("----Students & Exercises----")
for key, value in student_exercise_dict.items():
    print(f"    --{key} is working on:")

    for ex in value:
        print(f"        --{ex}")

    print("\n")
       
instructor_exercise_dict = data.get_student_exercise_dictionary('instructor')
print("----Instructors & Exercises----")
for key, value in student_exercise_dict.items():
    print(f"    --{key} assigned the following exercises: ")
    for ex in value:
        print(f"        --{ex}")
    
    print("\n")



print("----ADVANCED CHALLENGE EXERCISES, INSTRUCTORS AND STUDENTS----")
challenge_dict_for_both = data.get_student_exercise_dictionary("both")
for key, value in challenge_dict_for_both.items():
    print(f"    --{key}--")
    for pair in value:
        print(f"{pair[0]} assigned this to {pair[1]}")
    print("\n")

print("----ADVANCED CHALLENGE COHORTS, INSTRUCTORS AND STUDENTS----")
new_challenge_dict = data.get_students_cohorts_exercises()
print("\n")
for key, value in new_challenge_dict.items():
    print(f"--{key}--")
    print(f"    --Students--")
    for stud in value["students"]:
        print(f"{stud} is in {key}")
    print(f"    --Instructors")
    for inst in value["instructors"]:
        print(f"{inst} teaches {key}")
