# 4. Given a list : SRN, P_marks, C_marks, M_marks and B_marks.
# srns = ["EC003","EC013","EC036","EC033","EC023"]
# p_marks = [98,99,80,90,89], c_marks = [91,90,84,92,79]
# m_marks = [78,39,60,50,84], b_marks = [100,69,78,70,59]

# a) Create a dict with SRN as the key and marks in P, C, M, B as a value.
srns = ["EC003", "EC013", "EC036", "EC033", "EC023"]
p_marks = [98, 99, 80, 90, 89]
c_marks = [91, 90, 84, 92, 79]
m_marks = [78, 39, 60, 50, 84]
b_marks = [100, 69, 78, 70, 59]
student_details = {}; i = 0
for srn in srns:
    student_details[srn] = []
    student_details[srn].extend([p_marks[i], c_marks[i], m_marks[i], b_marks[i]])
    i = i + 1
for key in student_details:
    print(key, ':', student_details[key])

