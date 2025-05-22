names = ["Anna", "Bohdan", "Oksana", "Ivan"]
subjects = ["Math", "History", "Biology", "Physics"]
grades = [10, 8, 12, 9]


for name,sub,grade in zip(names,subjects,grades):
    print("{} {} grades: {}" .format(name,sub,grade))