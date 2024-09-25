#Christian Brown

def gradeCenter(name, score, id, **kwargs):
    student = {'Name': name, 'Score': score, 'id': id}
    for key, value in kwargs.items():
        student[key] = value
    return student


wcuStudent = gradeCenter('Functions-ReturnValues', 100, 14, completed='true')

print(wcuStudent)