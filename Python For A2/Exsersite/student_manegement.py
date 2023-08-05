n = int(input("Enter Number Of Student: "))

students = []

for i in range(n):
    student = {}

    print("Student: ", i + 1)
    student['id'] = input("Enter ID: ")
    student['name'] = input("Enter Name: ")
    student['sex'] = input("Enter Sex: ")
    student['cpp'] = float(input("Enter CPP: "))
    student['dsa'] = float(input("Enter DSA: "))
    student['dbs'] = float(input("Enter DBS: "))

    student['total'] = student['cpp'] + student['dsa'] + student['dbs']
    student['avg'] = student['total'] / 3

    if student['avg'] >= 90:
        student['grade'] = 'A'
    elif student['avg'] >= 80:
        student['grade'] = 'B'
    elif student['avg'] >= 70:
        student['grade'] = 'C'
    elif student['avg'] >= 60:
        student['grade'] = 'D'
    elif student['avg'] >= 50:
        student['grade'] = 'E'
    else:
        student['grade'] = 'F'

    students.append(student)

    print("Total: ", student['total'])
    print("AVG: ", student['avg'])
    print("Grade: ", student['grade'])

students.sort(key=lambda x: x['total'], reverse=True)

print("\n {:>50}".format("Students Information"))
print(" \n{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("ID", "Name"
                                                                               , "Sex", "CPP"
                                                                               , "DSA", "DBS"
                                                                               , "Total", "AVG"
                                                                               , "Grade"))

for student in students:
    print("{:<10} {:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10}".format(student['id']
                                                                                                   , student['name']
                                                                                                   , student['sex'],
                                                                                                   student['cpp']
                                                                                                   , student['dsa'],
                                                                                                   student['dbs']
                                                                                                   , student['total'],
                                                                                                   student['avg']
                                                                                                   , student['grade']))
