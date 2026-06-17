marks = float(input("enter your marks :"))
print("your entered marks is : ",marks)
if (marks < 0 or marks > 100) :
    print("Invalid marks")

elif(marks >= 90) :
    print("Grade A")

elif(marks >= 80 and marks < 90) :
    print("Grade B")

elif(marks >= 70 and marks < 80) :
    print("Grade C")

elif(marks >= 60 and marks < 70) :
    print("1st")

elif(marks >= 50 and marks < 60) :
    print("2nd")
    
elif(marks >= 40 and marks < 50) :
    print("3rd")

elif(marks >= 33 and marks < 40) :
    print("Pass")

else :
    print("Fail")







