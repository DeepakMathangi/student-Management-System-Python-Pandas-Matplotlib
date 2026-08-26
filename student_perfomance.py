import csv
import matplotlib.pyplot as plt
import pandas as pd


def create_csv():
    with open("studentdata.csv","w",newline="") as file:
       writer=csv.writer(file)
       writer.writerow([
        "student_name",
        "roll_no",
        "english_marks",
        "math_marks",
        "python_marks",
        "pps_marks",
        "attendance",
        "percentage",

    ])
create_csv()

def addstudent():
    student_name= input("Enter name of the student:")
    roll_no=input("enter roll no:")
    english_marks=input("enter english marks:")
    math_marks=input("enter maths marks:")
    python_marks=input("enter python marks:")
    pps_marks=input("enter pps marks:")
    attendance=input("enter attendance percentage:")
    p=((int(english_marks)+int(math_marks)+int(python_marks)+int(pps_marks))/400)*100
    percentage= p
    with open("studentdata.csv","a",newline="") as file:
         writer=csv.writer(file)
         writer.writerow([
           student_name,
           roll_no,
           english_marks,
           math_marks,
           python_marks,
           pps_marks,
           attendance,
           percentage,
        


    ])
    print("student added successfully")
def view_attendance():
    with open("studentdata.csv","r",newline="") as file:
        reader=csv.DictReader(file)
        for attendance in file:
            print("Attendance percentage:")
            print(attendance["attendance"])
       


def calculate_results():
    with open("studentdata.csv","r",newline="") as file:
            reader=csv.DictReader(file)
            for student in reader:

                english=int(student["english_marks"])
                maths=int(student["math_marks"])
                python=int(student["python_marks"])
                pps=int(student["pps_marks"])
                total=english+maths+python+pps
                print("Total marks:")
                print(total)
                cgpa=total/4
                print("CGPA:")
                print(float(cgpa))
               # return total,cgpa


def view_students():
    with open("studentdata.csv","r",newline="") as file:
        reader=csv.DictReader(file)
        for student in reader:
            print(
               "NAME", student["student_name"],
               "ROLL NO", student["roll_no"],
               "ENGLISH MARKS", student["english_marks"],
               "MATH MARKS",student["math_marks"],
               "PPS MARKS" ,student["pps_marks"],
               "ATTENDANCE", student["attendance"]
            )
create_csv()

#addstudent()
#view_students()
def StudentsATrisk():
     with open("studentdata.csv","r",newline="") as file:
          reader=csv.DictReader(file)
          for student in reader:
              if(float(student["attendance"])<75):
                    print(student["student_name"],"STUDENT AT RISK ZONE.Kindly requested to maintain atleast 75 percent")
              elif(float(student["attendance"])>75):
                  print("no issues with the attendance. GOOD ATTENDANCE PERCENTAGE")


def ResultAnalysis():
    df=pd.read_csv('studentdata.csv')
    x=df["student_name"]
    y=df["percentage"]
    plt.xlabel("student_data",fontsize=15)
    plt.ylabel("percentage",fontsize=16)
    plt.bar(x,y)
    plt.show()
def main():
    while True:
       print("Student Perfomace")
       print("----------------------------------")
       print("MENU",end="")
       print("------------------")
       print("1.Add student")
       print("2.view students")
       print("3.Semester Result")
       print("4.Students at risk")
       print("5.Result Analysis")
       choice=int(input("Enter your choice:"))
       match choice:
           case 1:
               addstudent()
           case 2:
               view_students()
           case 3:
               calculate_results()
           case 4:
               StudentsATrisk()
           case 5:
               ResultAnalysis()
           case _:
               print("invalid choice")
               break 
           
main()







                  
                    
                  
              
                     
                     
                            
                     
                            
                    
            


