from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

###### Exercises
flexbox = Exercise('Flex-box Froggy', "CSS")
itinerary = Exercise('Nashville Itinerary', "Javascript")
nutshell = Exercise('First Nutshell', "Javascript")
cars = Exercise('Cars', "Python")

##### Cohorts

cohort_37 = Cohort("Day Cohort 37", [], [] )
cohort_38 = Cohort("Day Cohort 38", [], [] )
cohort_39 = Cohort("Night Cohort 39", [], [] )

######Students

jim = Student('Jim', 'Halpert', 'lil_jimmy', 38, "Python tutorial", "React project")
dwight = Student('Dwight', "Shrute", 'beets_FTW', 37, 'C# gold', 'Chicken-Monkey')
pam = Student('Pam', 'Beasley', 'white_shoes_4Eva', 39, 'Css-grid', 'UI test')
creed = Student('Creed', "Bratton", 'www.creedthoughts.com/gov', 38, 'word-doc', 'puzzles')


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





