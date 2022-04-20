import numpy as np
from matplotlib import pyplot as plt

available_marks = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
marks = np.random.choice(available_marks, size=(22, 10))
print(marks)

number_of_subjects_to_check = int(input("Please pass number of subjects which you want to check: "))
how_many = 0
fives = []

for student in marks:

    ndst = 0
    for subject_mark in student:
        if subject_mark < 3.0:
            ndst += 1
        if number_of_subjects_to_check == ndst:
            how_many += 1
            break

print(f"Number of students who didn't pass given number of subjects: {how_many}")

the_best_student_average_grade = (max(marks.sum(axis=1))) / (marks.shape[1])
the_worst_student_average_grade = (min(marks.sum(axis=1))) / (marks.shape[1])
print(f"The best GPA: {the_best_student_average_grade}")
print(f"The worst GPA: {the_worst_student_average_grade}")

sums = marks.sum(axis=1)
current = []
for item in sums:
    current.append(item)

b = current.index(max(current))
w = current.index(min(current))

print(f"The best grades: {marks[b, :]} \nThe worst grades: {marks[w, :]}")

the_best_grade = marks.max()

for student in marks:
    best = 0

    for subject_mark in student:
        if subject_mark == the_best_grade:
            best += 1

    fives.append(best)

the_biggest_amount = max(fives)
presences = fives.count(the_biggest_amount)
indexes = []

if presences == 1:
    print(f"Student whose index is {fives.index(the_biggest_amount)} got the most the highest grades.")
else:
    for s in range(len(fives)):
        if fives[s] == the_biggest_amount:
            indexes.append(s)
    print(f"Students whose indexes are {indexes} got the most highest grades.")

students_higher_than_4 = []
i = 0
GPAs = marks.sum(axis=1) / marks.shape[1]

print(f'GPAs : {GPAs}')

while i < GPAs.shape[0]:
    if GPAs[i] >= 4.0:
        students_higher_than_4.append(i)
    i += 1
print(f"Students whose GPA is >= 4.0: {students_higher_than_4}")

h0 = marks[:, 0].flatten()
h1 = marks[:, 1].flatten()
h2 = marks[:, 2].flatten()


def converting(x):
    new_list = []
    for item in x:
        new_list.append(item)
    return new_list


maths_help = converting(h0)
physics_help = converting(h1)
IT_help = converting(h2)


def counter(y):
    stats = []
    for mark in available_marks:
        count = 0
        for m in y:
            if m == mark:
                count += 1
        stats.append(count)
    return stats


maths = counter(maths_help)
physics = counter(physics_help)
IT = counter(IT_help)

possible_marks = ["2", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5"]
x_p_m = np.arange(len(possible_marks))
width = 0.25

plt.bar(x_p_m - width, maths, width=width, color="#FFA07A", label="Maths")
plt.bar(x_p_m, physics, width=width, color="#BA55D3", label="Physics")
plt.bar(x_p_m + width, IT, width=width, color="#00FA9A", label="IT")

plt.xticks(ticks=x_p_m, labels=possible_marks)
plt.title("Grades")
plt.xlabel("Possible marks")
plt.legend()

plt.show()

