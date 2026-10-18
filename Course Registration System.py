import os
import datetime

# File Names
STUDENT_FILE = 'students.txt'
COURSE_FILE = 'courses.txt'
ENROLLMENT_FILE = 'enrollments.txt'

# Function to load data from a file (reading)
def load_data(filename):
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as file:  # Read file
            return [line.strip() for line in file.readlines()]  # Read and strip each line
    return []  # Return an empty list if the file does not exist

# Function to save data to file (writing)
def save_data(filename, data):  # Data: A list of strings to be written to the file.
    with open(filename, 'w') as file:  # Write mode
        for item in data:
            file.write(f"{item}\n")  # Writes each item to the file on a new line.

# Function to add a new student with ID and contact number validation
def add_student():
    while True:  # Loop to allow adding multiple students
        students = load_data(STUDENT_FILE)  # Load existing student data

        print("\n--- Add a New Student ---")
        print("Type '0' at any prompt to cancel.")

        # Validate Student ID (8-digit numbers only, student id is always unique)
    
        while True:
    
                student_id =input("Enter Student ID (8-digit numbers only): ")

                if student_id == '0':  # Exit condition
                    print("Operation cancelled. Returning to main menu.\n")
                    return
                
                if not student_id.isdigit():
                    print("Invalid Student ID! It must contain only numbers.\n")
                    continue

                if len(student_id) != 8:
                    print("Invalid Student ID! It must be exactly 8 digits.\n")
                    continue

                # Check for duplicate ID
                duplicate = any(student.startswith(student_id + ',') for student in students)

                if duplicate:
                    print("Student ID already exists! Please enter a unique ID.\n")
                    continue

                break
            
        # Validate Name (Only letters and spaces)
        while True:

                name = input("Enter Student Name: ").strip().upper() #convert name into uppercase

                if name == '0':  # Exit condition
                    print("Operation cancelled. Returning to main menu.\n")
                    return

                elif name.isdigit():
                    print("Invalid input! Name should only contain letters and symbols.\n")
                    continue

                break

        # Validate Contact Number (Minimum 7 digits, numbers only)
        while True:
            try: 
                contact = int(input("Enter Contact Number (minimum 7-digit numbers only): ").strip())

                if contact == 0:  # Exit condition
                    print("Operation cancelled. Returning to main menu.\n")
                    return

                if len(str(contact)) < 7:  # Check if only numbers and at least 7 digits
                    print("Invalid Contact Number! It must be at least 7 digits and contain only numbers.\n")
                    continue
                
            except ValueError:
                print("Invalid Contact Number! It must be at least 7 digits and contain only numbers.\n")
                continue
            
            break
                
        # Save student data
        student_data = f"{student_id},{name},{contact}"
        students.append(student_data)  # Add new student to the list
        save_data(STUDENT_FILE, students)  # Save updated student list
        print(f"\nStudent added successfully! Assigned ID: {student_id}\n")

        # Ask if user wants to add another student
        while True:
            proceed = input("Do you want to add another student? (yes/no): ").strip().lower()
            if proceed == "yes":
                break  # Restart loop to add another student
            elif proceed == "no":
                print("Returning to main menu.\n")
                return
            else:
                print("Invalid input! Please enter 'yes' or 'no'.\n")

# Function to add a new course with validation and duplicate ID check
def add_course():
    courses = load_data(COURSE_FILE)  # Load existing course data

    print("\n--- Existing Courses ---")
    if not courses:
        print("No courses added yet.\n")

    else:
        # Properly display all loaded courses
        for course in courses:
                course_id, name, max_seats,remaining_seats = course.split(',')
                print(f"Course ID: {course_id}, Name: {name}, Seats Available: {remaining_seats}")

    print("\n--- Add a New Course ---")
    print("Type '0' at any prompt to cancel.")

    while True:
        course_id = input("Enter Course ID (letters and numbers only): ").strip().upper()
        if course_id == "0":
            print("Operation cancelled. Returning to main menu.\n")
            return
            
        if not course_id.replace(" ", "").isalnum():  # Ensures only letters and numbers
            print("Invalid input! Course ID should contain only letters and numbers.\n")
            continue
        
        #Check for duplicate Course ID
        if any(course.startswith(course_id + ',') for course in courses):
            print("Course ID already exists! Please enter a unique Course ID for the course.\n")
            continue
        
        break
            
    #Prompt user to enter course name
    while True:
        course_name = input("Enter Course Name: ").strip().upper()

        if course_name == "0":
            print("Operation cancelled. Returning to main menu.\n")
            return
            
        if course_name.replace(" ", "").isalpha():  # Ensures only letters
            break
        
        else:
            print("Invalid input! Course Name should only contain letters.\n")

    while True:
        max_seats = input("Enter Maximum Seats (numbers only): ").strip()

        if max_seats == '0':  # Exit condition
            print("Operation cancelled. Returning to main menu.\n")
            return

        if max_seats.isdigit():  # Ensures only numbers
            break
        else:
            print("Invalid input! Maximum Seats should be a number.\n")

    # Save course data 
    # max_seats (again) → It is duplicated, likely used to store remaining seats (initially equal to max_seats).
    course_data = f"{course_id},{course_name},{max_seats},{max_seats}"  
    courses.append(course_data)  # Adds the newly created course_data string to the courses list.
    save_data(COURSE_FILE, courses)  # Calls a function named save_data() to save the updated courses list into a file
    print("Course added successfully!\n")

    # Show updated course list after addition
    print("--- Updated Course List ---")
    for course in courses:
        course_id, name, max_seats, remaining_seats = course.split(',')
        print(f"Course ID: {course_id}, Name: {name}, Seats Available: {remaining_seats}")

    # Ask if user wants to add another course
    while True:
        proceed = input("Do you want to add another course? (yes/no): ").strip().lower()
        if proceed == "yes":
            add_course()
            return
        elif proceed == "no":
            print("Returning to main menu.\n")
            return
        else:
            print("Invalid input! Please enter 'yes' or 'no'.\n")

# Enroll in Course
def enroll_course():
        students = load_data(STUDENT_FILE) #load student data
        courses = load_data(COURSE_FILE)  # load data from course file
        enrollments = load_data(ENROLLMENT_FILE) #load enrollment data

        #Check if there are any existing courses
        if not courses:
            print("There are currently no available courses to enroll.\n")
            return
              
        print("Type '0' at any prompt to cancel.")
        student_id = input("Enter Student ID: ").strip()

        if student_id == '0':  # Exit condition
            print("Operation cancelled. Returning to main menu.\n")
            return

        #Check if the student ID exists in the students file
        student_exists = any(student.startswith(student_id + ',')for student in students)

        if not student_exists:
            print("Student ID not found! Please register as a student first.")
            print("When you are back in the menu, press 1 to register as a student.\n")
            return
    
        print("--- Existing Course List ---")

        for course in courses:
            course_id, name, max_seats, remaining_seats = course.split(',')
            print(f"Course ID: {course_id}, Name: {name}, Seats Available: {remaining_seats}")

        course_id = input("Enter Course ID: ").strip().upper()

        if course_id == "0":
            print("Operation cancelled. Returning to main menu.\n")
            return

        #check if student is already enrolled in the course
        for enrollment in enrollments:
            sid, cid, date = enrollment.split(',')
            if sid == student_id and cid.upper() == course_id:
                print("You have already registered for this course. Please enroll other courses.\n")
                return
        
        enrolled = False
        updated_courses = []
        
        for course in courses:
            cid, name, max_seats, remaining_seats = course.split(',')
            if cid.upper() == course_id:
                if int(remaining_seats) > 0:  # Checks if cid matches course_id (ensuring it's the correct course).
                    remaining_seats = str(int(remaining_seats) - 1)  # Decreases available seats by 1.
                    enrolled = True  # Marks enrolled = True to indicate successful enrolment.
                else:
                    print("No seats available for this course.\n")
                    return
            updated_courses.append(f"{cid},{name},{max_seats},{remaining_seats}")
            # After modifying the remaining_seats, the updated course details are stored in updated_courses.

        if enrolled:
            save_data(COURSE_FILE, updated_courses)  # Save updated course data
            enrollments.append(f"{student_id},{course_id},{datetime.date.today()}")  # datetime.date.today() (stores the current date of enrolment).
            save_data(ENROLLMENT_FILE, enrollments)  # Save updated enrollments
            print("Enrollment successful!\n")
        
        else:
            print("Course not available or invalid course ID!\n")  # The course does not exist OR The course has no available seats.

        # Ask if user wants to enroll to another course
        while True:
            proceed = input("Do you want to enroll to another course? (yes/no): ").strip().lower()
            if proceed == "yes":
                enroll_course()
                return
            elif proceed == "no":
                print("Returning to main menu.\n")
                return
            else:
                print("Invalid input! Please enter 'yes' or 'no'.\n")

# Drop a Course
def drop_course():
    students = load_data(STUDENT_FILE) #load student data
    courses = load_data(COURSE_FILE)  # load data from course file
    enrollments = load_data(ENROLLMENT_FILE) #load enrollment data

    #Check if there are any courses available
    if not courses:
        print("There are currently no available courses to drop.\n")
        return

    print("Type '0' at any prompt to cancel.")
    student_id = input("Enter Student ID: ")

    if student_id == "0":
        print("Operation cancelled. Returning to main menu.\n")
        return

    #Check if the student ID exists in the students file
    student_exists = any(student.startswith(student_id + ',') for student in students)

    if not student_exists:
        print("Student ID not found! Please register as a student first.")
        print("When you are back in the menu, press 1 to register as a student.\n")
        return

    #Check if the student had enrolled to any course
    student_enrolled_courses = []

    for enrollment in enrollments:
        sid, cid = [x.strip() for x in enrollment.split(',')[:2]] #extract student
        if sid == student_id: #Check if this enrollment belongs to the student
            student_enrolled_courses.append(cid)

    if not student_enrolled_courses:
        print("You are not enrolled in any courses yet.\n")
        return

    #Display enrolled courses
    print("\nYou are currently enrolled in the following courses: ")
    displayed_courses = set()
    for course in courses:
        cid, name, max_seats, remaining_seats = course.split(',')
        if cid in student_enrolled_courses and cid not in displayed_courses:
            print(f"{cid}, {name.strip()}")
            displayed_courses.add(cid)

    course_id = input("\nEnter Course ID to drop: ").strip().upper()

    if course_id == "0":
        print("Operation cancelled. Returning to main menu.\n")
        return
  
    #Check if the course
    if course_id not in student_enrolled_courses:
        print("You are not enrolled in this course.")
        return
    
    updated_enrollments = []  # Create empty list to store updated enrollment data
    
    for enrollment in enrollments:
        sid, cid, date = enrollment.split(',')
        if not (sid == student_id and cid == course_id):
            updated_enrollments.append(enrollment)  # Keep the enrollment record in updated_enrollments.
    
    updated_courses = []  # List to store updated course data
        
    for course in courses:  # Loops through each course in courses
        cid, name, max_seats, remaining_seats = course.split(',')
        if cid == course_id:  # If the course being dropped is found
            remaining_seats = str(int(remaining_seats) + 1)  # Increase available seats by 1.
        updated_courses.append(f"{cid},{name},{max_seats},{remaining_seats}")  # Add the updated course data back into updated_courses.

    save_data(ENROLLMENT_FILE, updated_enrollments)  # Save the updated enrollment list (excluding the dropped course).
    save_data(COURSE_FILE, updated_courses)  # Save the updated course list (with increased seat availability).
    print("Course dropped successfully!\n")

    # Ask if user wants to enroll to another course
    while True:
        proceed = input("Do you want to enroll to another course? (yes/no): ").strip().lower()
        if proceed == "yes":
            drop_course()
            return
        elif proceed == "no":
            print("Returning to main menu.\n")
            return
        else:
            print("Invalid input! Please enter 'yes' or 'no'.\n")
        
  # View Available Courses
def view_courses():
    courses = load_data(COURSE_FILE)
    print("Available Courses:")

    # Condition to check if no courses are available
    if not courses:  # Checks if courses list is empty
        print("No courses available at the moment!\n")
        return  # Exit function early

    for course in courses:
        course_id, name, max_seats, remaining_seats = course.split(',')
        print(f"Course ID: {course_id}, Name: {name}, Seats Available: {remaining_seats}")
    print()  # Add blank line for readability

# View Student Information
def view_students():
    students = load_data(STUDENT_FILE)

    if not students:  # Checks if students list is empty
        print("No students registered at the moment!\n")
        return  # Exit function early
    
    print("Registered Students:")
    for student in students:  # student list
            student_id, name, contact = student.split(',')
            print(f"Student ID: {student_id}, Name: {name}, Contact: {contact}")
    print()  # Add blank line for readability

# Menu System
def main_menu():
    while True:
        print("Course Registration System")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enroll in Course")
        print("4. Drop Course")
        print("5. View Available Courses")
        print("6. View Students")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            enroll_course()
        elif choice == '4':
            drop_course()
        elif choice == '5':
            view_courses()
        elif choice == '6':
            view_students()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.\n")

if __name__ == '__main__':
    main_menu()
                                                
