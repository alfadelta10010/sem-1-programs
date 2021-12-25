# c) create a dict with M_marks as the key and srn of the students as
# value.
srns = ["EC003", "EC013", "EC036", "EC033", "EC023"]
p_marks = [98, 99, 80, 90, 89]
c_marks = [91, 90, 84, 92, 79]
m_marks = [78, 39, 60, 50, 84]
b_marks = [100, 69, 78, 70, 59]
i = 0; student_details = {}
for srn in srns:
    if m_marks[i] not in student_details:
        student_details[m_marks[i]] = []
        student_details[m_marks[i]].append(srn)
    i = i + 1
for key in student_details:
    print(key, ':', student_details[key])
