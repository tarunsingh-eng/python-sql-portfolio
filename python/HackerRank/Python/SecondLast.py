# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.



if __name__ == '__main__':
    students = []
    for i in range(int(input("Total number of entries "))):
        name = input("Name of Student ")
        score = float(input("Student Score "))
        students.append([name,score])
    
    # print (name)
    # print (score)
    
    scores = []
    
    for student in students:
        scores.append(student[1])
        
    scoreset = sorted(set(scores))
    secondbest = []
    for student in students:
        if (student[1]==scoreset[1]):
                secondbest.append(student[0])
    secondbest = sorted(secondbest)
    for name in secondbest:
        print("Second last student is "+name)