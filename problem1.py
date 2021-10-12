
def letter_grade(numerical_score):
    if numerical_score > 100 or numerical_score<0:
        raise ValueError
    elif numerical_score >= 85:
        grade_point=4.00
        return 'A⁺', grade_point
    elif numerical_score >= 80:
        grade_point=4.00
        return 'A', grade_point
    elif numerical_score >= 75:
        grade_point=3.50
        return 'B⁺', grade_point
    elif numerical_score >= 70:
        grade_point=3.00
        return 'B', grade_point
    elif numerical_score >= 65:
        grade_point=2.50
        return 'C⁺', grade_point
    elif numerical_score >= 60:
        grade_point=2.00
        return 'C', grade_point
    elif numerical_score >= 55:
        grade_point=1.50
        return 'D⁺', grade_point
    elif numerical_score >= 50:
        grade_point=1.00
        return 'D', grade_point
    elif numerical_score <= 49:
        grade_point=0.00
        return 'E', grade_point
    
# test1=letter_grade(85)
# test2=letter_grade(72)
# test3=letter_grade(66)
# test4=letter_grade(75)
# test5=letter_grade(52)
# test6=letter_grade(35)

# test7=letter_grade(60)
# test8=letter_grade(58)
# print("test1: ", test1 )
# print("test2: ", test2)
# print("test3: ", test3)
# print("test4: ", test4)
# print("test5: ", test5)
# print("test6: ", test6)
# print("test7: ", test7)
# print("test8: ", test8)




honor1='Summa Cum Laude'
honor2='Magna Cum Laude'
honor3='Cum Laude'
def honour_categories(cum_grade_point_avg):
    if cum_grade_point_avg >=3.85:
        return honor1
    elif cum_grade_point_avg >= 3.70:
        return honor2
    elif cum_grade_point_avg >= 3.50:
        return honor3
    else:
        return 'No honor'
    

# check1=honour_categories(3.89)
# check2=honour_categories(3.77)
# check3=honour_categories(3.65)
# check4=honour_categories(2.25)
# print("check1: ", check1)
# print("check2: ", check2)
# print("check3: ", check3)
# print("check4: ", check4)


def student_grade():
    num_courses=int(input("Please enter the number of courses: "))
    num_A_plus=0
    num_As=0
    num_B_plus=0
    num_Bs=00
    num_C_plus=0
    num_Cs=0
    num_D_plus=0
    num_Ds=0
    num_Es=0
    cumulative_Grade_Points=[]                                      #storing all the grade points in a list
    for i in range(num_courses):
        numerical_score=float(input("Enter the score for a subject #" +str(i+1) + " "))
        subject=letter_grade(numerical_score)
        cumulative_Grade_Points.append(subject[1])
        print(f" Your grade for subject {str(i+1)} is {subject[0]} and is worth a gradepoint of {subject[1]}")
        if subject[0]=='A⁺':
            num_A_plus=1
        elif subject[0]=='A':
            num_As+=1
        elif subject[0]=='B⁺':
            num_B_plus+=1
        elif subject[0]=='B':
            num_Bs+=1
        elif subject[0]=='C⁺':
            num_C_plus+=1
        elif subject[0]=='C':
            num_Cs+=1
        elif subject[0]=='D⁺':
            num_D_plus+=1
        elif subject[0]=='D':
            num_Ds+=1
        elif subject[0]=='E':
            num_Es+=1
            
    Total_cumulative_Grade_Points=round(float(sum(cumulative_Grade_Points)), 2)
    cumulative_Grade_Points_Average=round(Total_cumulative_Grade_Points/num_courses, 2)
    
    print("You obtained",num_A_plus,"A+s, ", num_As, "As, ", num_B_plus, "B+s, ",num_Bs, "Bs, ", num_C_plus, "C+s, ", num_Cs, "Cs, ", num_D_plus, "D+s, ", num_D_plus,"Ds, ",  "and ", num_Es, "Es")
    Total_cumulative_Grade_Points=round(float(sum(cumulative_Grade_Points)), 2)
    cumulative_Grade_Points_Average=round(Total_cumulative_Grade_Points/num_courses, 2)
    print(f"\nYour cumulative_Grade_Point_Average is {cumulative_Grade_Points_Average}")
    print("\nYou won ", honour_categories(cumulative_Grade_Points_Average))
    
    
student_grade()
    
        