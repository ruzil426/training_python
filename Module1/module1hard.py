grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a = (sum(grades[0]), sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4]))
print(a)
b = (len(grades[0]), len(grades[1]), len(grades[2]), len(grades[3]), len(grades[4]))
print(b)
c = (float(a[0] / (b[0])), float(a[1] / (b[1])), float(a[2] / (b[2])), float(a[3] / (b[3])), float(a[4] / (b[4])))
print(c)

students = sorted(students)

average_grades = dict(zip(students, c))
print(average_grades)


