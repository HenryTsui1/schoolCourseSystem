'''Provides instruction to user when they would like to create a new course'''
def newCourse(course_list):
    new_course = [] #adds items to this list, to create new course
    print("To create new course, please follow the instructions precisely...")
    while True:
        userCode = input("Enter course code following the format AAAA###: ")
        if len(userCode) == 7 and userCode[0:4].isalpha() and userCode[-3:].isdigit():
            new_course.append(userCode) #adds to new_course
            break #breaks out of while loop after it satifies the condition
        print("Invalid course code format")
    while True:
        userDepart = input("Enter department for the new course: ")
        if userDepart.isalpha():
            new_course.append(userDepart)
            break
        print("Invalid input for department")
    while True:
        userInstruct = input("Please enter the instructor's name for this new course: ")
        if userInstruct.isalpha(): #checking to see if the input are strings, appropriate name format
            new_course.append(userInstruct)
            break
        print("Invald input for instructor")
    while True:
        userCapacity = input("Please enter the maximum capacity for this new course: ")
        if userCapacity.isdigit():
            new_course.append(userCapacity)
            break
        print("Invalid input for occupancy")
    while True:
        userEnroll = input("Please enter the number of enrolled students for this new course: ")
        if userEnroll.isdigit() and userEnroll <= userCapacity:
            new_course.append(userEnroll)
            break
        print("Invalid input for enrolled students")
    if userCapacity == userEnroll: #if the numbers are equal to each other, add 'Full' to new_course
        new_course.append('Full')
    if userCapacity > userEnroll: #if enrolled students is less than the maximum capacity, adds 'available' to new_course
        new_course.append('Available')
    print('')
    print("New course added!")
    print('')
    print('Information for new course',new_course)
    course_list.append(new_course) #adds to the course_list, which is the database itself


'''Allows the user to update any courses available in the coures_list'''
def updateCourse(course_list):
    course_check = True
    while course_check:
        userinput = input("Enter course ID: ")
        for i in range(len(course_list)):
            if userinput.lower() == course_list[i][0].lower(): #if user input matches with the first element in the lists, breaks out of the loop
                course_row = course_list[i] #assigns the list as a variable to call on later 
                course_check = False
        if course_check:
            print("Invalid input, course does not exist.")

    update = True

    instructor = False
    enroll = False

    while update: #allows the user to change one of the following, the instructor or number of enrolled students
        userupdate = int(input("Enter 1 to update instructor, or enter 2 to update number of enrolled students: "))
        if userupdate == 1:
            instructor = True
            break
        elif userupdate == 2:
            enroll = True
            break


    while instructor: #can make changes to the instructor
        userInstruct = input("Enter the instructor's name: ")
        if userInstruct.isalpha():
            course_row[2] = userInstruct
            print("Information updated!")
            instructor = False
        else:
            print("Invalid name input") #only if the input is something other then a string

    while enroll: #changes number of enrolled students
        try:
            userEnroll = input("Enter number of enrolled students: ")
            if int(userEnroll) > int(course_row[-3]):
                print("Number of enrolled students can not be greater than the maximum capacity")
            elif int(userEnroll) == int(course_row[-2]): #if the current number of enrolled students is same as user input, informs the user
                print("No changes were made, number of enrolled students is still",course_row[-2])
            elif int(userEnroll) <= int(course_row[-3]):
                print("Information updated!")
                course_row[4] = userEnroll
                enroll = False
        except:
            print("Invalid input")
    

    print(course_row) #displays the updated information
                