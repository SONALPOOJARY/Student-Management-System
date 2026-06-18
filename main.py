import os

filename = "Database.txt"


class Student:

    def __init__(self, name, roll_number, marks):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = marks


    @property
    def name(self):
        return self.__name


    @property
    def roll_number(self):
        return self.__roll_number


    @property
    def marks(self):
        return self.__marks


    def get_average(self):
        return sum(self.__marks) / len(self.__marks)


    def is_pass(self):

        if self.get_average() >= 40:
            return "Pass"

        else:
            return "Fail"


    def __str__(self):
        return f"Name: {self.name} | Roll: {self.roll_number} | Avg: {self.get_average():.2f} | Status: {self.is_pass()}"


    def search_display(self):
        return f"""
Name: {self.name}
Roll Number: {self.roll_number}
Marks: {self.marks}
Average: {self.get_average():.2f}
Status: {self.is_pass()}
"""


def file():

    try:

        if os.path.exists(filename):

            print("File exists! You can continue with operations.")

        else:

            raise FileNotFoundError("File does not exist!")

    except FileNotFoundError as e:

        print(e)

        print("Creating a new file...")

        with open(filename, "w"):
            pass

        print("New file created successfully!")



def Add_Student():

    name = input("Enter student name:")


    while True:

        roll_number = input("Enter roll number:")


        exists = False


        with open(filename,"r") as f:

            for line in f:

                data = line.strip().split(",")

                if len(data)>1 and data[1] == roll_number:

                    exists = True
                    break


        if exists:

            print(f"Roll number {roll_number} already exists!")

        else:

            break



    marks = []


    for i in range(1,4):

        while True:

            try:

                mark = int(input(f"Enter mark {i} (0-100): "))


                if mark < 0 or mark > 100:

                    raise ValueError("Invalid marks! Must be between 0 to 100")


                marks.append(mark)

                break


            except ValueError as e:

                print(e)



    with open(filename,"a") as f:

        f.write(f"{name},{roll_number},{marks[0]},{marks[1]},{marks[2]}\n")


    print("Student Successfully Added!!!")


def View_All_Students():

    with open(filename,"r") as f:

        content = f.read()


    if len(content.strip()) == 0:

        print("❌ No students found!")
        return


    total_students = 0
    total_pass = 0
    total_fail = 0


    with open(filename,"r") as f:

        print("========== All Students ==========")


        for line in f:

            data = line.strip().split(",")


            name = data[0]
            roll = data[1]


            marks = []

            for mark in data[2:]:

                marks.append(int(mark))


            s = Student(name, roll, marks)


            print(s)


            total_students += 1


            if s.is_pass() == "Pass":

                total_pass += 1

            else:

                total_fail += 1



    print("==================================")

    print(f"Total students: {total_students} | Pass: {total_pass} | Fail: {total_fail}")



def Search_Student():

    roll_number = input("Enter roll number to search:")


    with open(filename,"r") as f:

        for line in f:


            data = line.strip().split(",")


            if len(data)>1 and data[1] == roll_number:


                name = data[0]

                marks = []


                for mark in data[2:]:

                    marks.append(int(mark))


                s = Student(name, roll_number, marks)


                print("========== Student Found ==========")

                print(s.search_display())

                print("==================================")

                return



    print(f"Student with roll number {roll_number} not found!")



def Delete_Student():

    roll_number = input("Enter roll number to delete:")


    found = False


    with open(filename,"r") as f:

        lines = f.readlines()



    with open(filename,"w") as f:


        for line in lines:


            data = line.strip().split(",")


            if len(data)>1 and data[1] == roll_number:


                found = True

                continue


            f.write(line)



    if found:

        print("Student deleted successfully!")

    else:

        print(f"Student with roll number {roll_number} not found!")




def Show_Topper():

    topper = None
    highest_average = 0


    with open(filename, "r") as f:

        content = f.read()


    if len(content.strip()) == 0:

        print("❌ No students found!")
        return


    with open(filename, "r") as f:

        for line in f:

            data = line.strip().split(",")

            name = data[0]
            roll = data[1]


            marks = []

            for mark in data[2:]:

                marks.append(int(mark))


            s = Student(name, roll, marks)


            if s.get_average() > highest_average:

                highest_average = s.get_average()

                topper = s



    print("========== 🏆 Topper ==========")

    print(topper.search_display())

    print("================================")





print("""
===== Student Management System =====
1. Add Student
2. View All Students
3. Search Student by Roll Number
4. Delete Student
5. Show Topper
6. Exit
=====================================
""")

file()
while True:

    try:

        choice = int(input("Enter your choice: "))


        if choice not in range(1,7):

            raise ValueError("Invalid Menu choice! Please enter between 1-6\n")


        if choice == 1:

            Add_Student()
            print("\n")


        elif choice == 2:

            View_All_Students()
            print("\n")


        elif choice == 3:

            Search_Student()
            print("\n")

        elif choice == 4:

            Delete_Student()
            print("\n")

        elif choice == 5:

            Show_Topper()
            print("\n")

        elif choice == 6:
            print("👋..Thank you for using Student Management System! Goodbye!")

            break



    except ValueError as e:

        print(e)
