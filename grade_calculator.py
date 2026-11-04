# 1. Take a student name as input
student_name = input("Enter student name: ")

# 2. Takes marks for three subjects 
math_marks = float(input("Enter Math marks: "))
english_marks = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

if (math_marks < 0 or math_marks > 100) or \
    (english_marks < 0 or english_marks > 100) or \
        (python_marks < 0 or python_marks > 100): 
            print("\nError: Invalid marks ! marks must be between 0 and 100. ")
else: 
    
    # 3. Calculate average marks 
    
    average_marks = (math_marks + english_marks + python_marks) / 3 
    
    # 4. Determine the grade using the given conditions
    if 80 <= average_marks <= 100:
        grade = "A+"
    elif 70 <= average_marks <= 79: 
        grade = "A"
    elif 60 <= average_marks <= 69:
        grade = "A-"
    elif 50 <= average_marks <= 59:
        grade = "B" 
    elif 40 <= average_marks <= 49: 
        grade = "C"    
    else: 
        grade = "F"  
        
# 5. Display the students's Name, average marks and final grades  
print(f"\nStudent Name: {student_name}")  
print(f"Average Marks: {average_marks: .2f}")   
print(f"Final Grade: {grade}")      
