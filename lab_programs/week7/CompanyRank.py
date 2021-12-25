# 7. Write a Python program to concatenate following
# dictionaries to create a new dictionary CompanyBiography.

comp_rank = {'Infosys': 1, 'Accenture': 2, 'Wipro': 3, 'TCS': 4, 'IBM': 5}
comp_found = {'N R Narayana Murthy': 1981, 'Clarence DeLany': 1989,
              'M.H. Hasham Premji': 1945, 'Sri Ratan Tata': 1868,
              'Charles Ranlett Flint': 1911}

comp_biography = {}
for detail in (comp_rank, comp_found):
    comp_biography.update(detail)
print("The complete Biography of top companies in Bangalore is:")

for key in comp_biography:
    print(key, ':', comp_biography[key])