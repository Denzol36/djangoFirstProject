grade = 0 
correct_answers = ['A', 'C', 'B', 'D', 'A', 'B', 'C', 'C', 'D', 'A']
student_answers = ['A', 'C', 'A', 'D', 'B', 'B', 'C', 'D', 'D', 'A']


for i,j in zip(correct_answers,student_answers):
    if i==j:
        grade+=1
        
print(grade)