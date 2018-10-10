COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(arg):
    output = []
    for key, value in COURSES.items():
        if value & arg:
            output.append(key)
    return output
print(covers({'Python'})) 

def covers_all(topics):
    courses_list = []    
    for course, values in COURSES.items():
        if(values & topics)  == topics:
            courses_list.append(course)

    return courses_list
print(covers_all({"conditions", "input"}))    