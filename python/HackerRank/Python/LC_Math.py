# Question:
# You are given a list of student records.
# Each record contains: name , subject , score
#
# Task:
# Using list comprehension, find all student names where:
# - subject is "Math"
# - score is 80 or more
#
# Return the result as a list of names.

records = [
    "Aman,Math,85",
    "Riya,Science,90",
    "Karan,Math,72",
    "Sneha,Math,95",
    "Vikram,English,88"
]

result = [
    #Answer
    name for record in records for name, subject, marks in [record.split(",")] if int(marks)>=80 and subject =='Math'

]

print(result)