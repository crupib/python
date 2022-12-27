# This solution is not efficient enough to pass all test cases in time.
# grade_of can take n steps, and we call it about n^2 times,
# so this is an O(n^3) algorithm.


def grade_of(desks, left, right):
    """
    desks is a list of desks; each desk is a list of two grades.
    left and right are valid indices in desks.

    If a grade appears in all desks[left:right+1], return the minimum such grade;
    otherwise, return 0.
    """
    grades = [desks[left][0], desks[left][1]]
    grades.sort()  # So that we process smaller grade first
    for grade in grades:
        ok = True
        for i in range(left, right + 1):
            if desks[i][0] != grade and desks[i][1] != grade:
                ok = False
        if ok:
            return grade
    return 0


n = int(input())

desks = []

for i in range(n):
    desk = input().split()
    desk[0] = int(desk[0])
    desk[1] = int(desk[1])
    desks.append(desk)

max_students = 0
smallest_grade = 0

for i in range(n):
    for j in range(i, n):
        if j - i + 1 > max_students:
            grade = grade_of(desks, i, j)
            if grade > 0:
                max_students = j - i + 1
                smallest_grade = grade

print(max_students, smallest_grade)
