# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(teachers):
    count = 0
    for teacher in teachers:
        count += 1
    return count

def num_courses(teachers):
    return sum(len(v) for v in teachers.values())

def courses(teachers):
    output = []
    for courses in teachers.values():
        output +=courses
    return output
#Create a function named most_courses that takes our good ol' teacher dictionary.
#most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.

def most_courses(teachers):
    max_count = 0
    starTeacher = ""
    for teacher, course_list in teachers.items():
        if len(course_list) > max_count:
            max_count = len(course_list)
            starTeacher = teacher
    return starTeacher
#it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(teachers):
    all_courses = []
    for teacher in teachers:
        all_courses.append([teacher, len(teachers[teacher])])
    return all_courses
    