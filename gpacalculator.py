
# computing for students letter grade and grade_point
def letter_grade_gradepoint(nummerical_grade):
    if nummerical_grade >= 85:
        grade_point=4.00
        return 'A⁺', grade_point
    elif nummerical_grade >= 80:
        grade_point=4.00
        return 'A', grade_point
    elif nummerical_grade >= 75:
        grade_point=3.50
        return 'B⁺', grade_point
    elif nummerical_grade >= 70:
        grade_point=3.00
        return 'B', grade_point
    elif nummerical_grade >= 65:
        grade_point=2.50
        return 'C⁺', grade_point
    elif nummerical_grade >= 60:
        grade_point=2.00
        return 'C', grade_point
    elif nummerical_grade >= 55:
        grade_point=1.50
        return 'D⁺', grade_point
    elif nummerical_grade >= 50:
        grade_point=1.00
        return 'D', grade_point
    elif nummerical_grade <= 49:
        grade_point=0.00
        return 'E', grade_point


# storing honors with variables
honor1='Summa Cum Laude'
honor2='Magna Cum Laude'
honor3='Cum Laude'

# determining the honour categories of students
def honour_categories(cum_grade_point_avg):
    if cum_grade_point_avg >=3.85:
        return honor1
    elif cum_grade_point_avg >= 3.70:
        return honor2
    elif cum_grade_point_avg >= 3.50:
        return honor3
    else:
        return 'No honor'


# receiving course information from students and calculaing for grade_pointsAor
def student_grade():
    num_courses=int(input("Please enter the number of courses: "))
    num_A_plus=0
    num_As=0
    num_B_plus=0
    num_Bs=0
    num_C_plus=0
    num_Cs=0
    num_D_plus=0
    num_Ds=0
    num_Es=0
    grade_points=[]
    credit_wieght_list=[]
    grade_point_multiply_by_credit_weight_list=[]
    for i in range(num_courses):
        
        num_score=float(input("Enter the score for a subject #" + str(i + 1) + " "))
        credit_weight=float(input("Enter the credit weight for the course #" + str(i + 1) + " "))
        credit_wieght_list.append(credit_weight)
       
        subject=letter_grade_gradepoint(num_score)
        grade_points.append(subject[1])
        print(f"Your grade for subject {str(i+1)} is {subject[0]} and is worth a gradepoint of {subject[1]}")
        if subject[0]=='A⁺':
            num_A_plus += 1
        elif subject[0]=='A':
            num_As += 1
        elif subject[0]=='B⁺':
            num_B_plus+=1
        elif subject[0]=='B':
            num_Bs += 1
        elif subject[0]=='C⁺':
            num_C_plus+=1
        elif subject[0]=='C':
            num_Cs += 1
        elif subject[0]=='D⁺':
            num_D_plus += 1
        elif subject[0]=='D':
            num_Ds += 1
        elif subject[0]=='E':
            num_Es += 1
    
    for credit, grade_point in zip(credit_wieght_list, grade_points):
        credit_by_grade_point= credit*grade_point
        grade_point_multiply_by_credit_weight_list.append(credit_by_grade_point)
    
    Total_grade_point=round(sum(grade_point_multiply_by_credit_weight_list), 2)
    cum_grade_point_average=round(Total_grade_point/sum(credit_wieght_list), 2)
   
    
    print("You obtained",num_A_plus,"A+s, ", num_As, "As, ", num_B_plus, "B+s, ",num_Bs, "Bs, ", num_C_plus, "C+s, ", num_Cs, "Cs, ", num_D_plus, "D+s, ", num_D_plus,"Ds, ",  "and ", num_Es, "Es")
    print(f"\nYour cumulative_Grade_Point_Average is {cum_grade_point_average}")
    print("\nYou won ", honour_categories(cum_grade_point_average))
    
    
student_grade()
    
        