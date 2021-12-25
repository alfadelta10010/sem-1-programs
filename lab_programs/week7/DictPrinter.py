# 1. Create dictionaries with at-least 3-5 entries for the following types and display the members.
# Student: Key: Subject code, Value: Student Name.
# Stock Report: Key: Ticker symbol, Value: Company Name.
# Google Pay: Key: Bank Account Number Values:(name, Rewards earned)
student = {'CS210': 'Nethra', 'EC299': 'Arun', 'EC211': 'Kishore', 'ME175': 'Megharaj', 'EE233': 'Anirudh'}
stock_report = dict(
    {'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK': 'Eastman Kodak', 'HPE': 'Hewlett-Packard Enterprise',
     'MCD': 'McDonald''s'})

GooglePay = {'CNB190015678': ('Aditya', 450), 'KB1600156799': ('Kavya', 1000), 'SBI1850625384': ('Suresh', 2000),
             'PB1200045671': ('Dhruv', 2000), 'SBI1200045678': ('Abhishek', 5000)}
print("The Student subject codes and names are:")
print("Key(Subject Code) : Value(Student_Name)")
for key in student:
    print(key, ':', student[key])
print("The stock report details are:")
print("Key (Ticker Code) : Value (Company Name)")
for key in stock_report:
    print(key, ':', stock_report[key])
print("The Google Pay reward details are:")
print("Key(Bank_account_Number) : Value(UserName,Rewards)")
for key, value in GooglePay.items():
    print(key, ':', value)
