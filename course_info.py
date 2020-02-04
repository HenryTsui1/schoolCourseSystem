'''Allows the user to view all the courses by calling on the list, or if 
they would like to search by category relating to the specified course'''

def infoCourse(course_list):
    searching = True    
    while searching:
        print("Enter 'all' if you would like to view all courses in the data base, or enter ")
        userinput = input("the instructor name, department, 'full', or 'available' to find specific courses: \n")
        for i in range(len(course_list)):
            if userinput == "all":  #when user input is 'all', prints out the entire course_list
                print(course_list[i])
                searching = False
            
            elif userinput.lower() == course_list[i][1].lower(): #search by department
                print(course_list[i])
                searching = False
                
            elif userinput.lower() == course_list[i][2].lower(): #search by instructor
                print(course_list[i])
                searching = False

            elif userinput.lower() == course_list[i][-1].lower():  #if user input is 'full' or 'available', displays the courses respectively
                print(course_list[i])
                searching = False
        
        if searching == True:
            print('')
            print('Invalid input')  #if none of the input matches the if statements, prints out 'invalid input'
            print('')

    
'''User is able to retrieve certain information from a course'''
def retrieveCourse(course_list): 
    retrieving = True
    while retrieving:
        userinput = input("Enter a valid course ID or department to retrieve course information:\n")
        for i in range(len(course_list)):
            if userinput.lower() == course_list[i][0].lower(): #if user input matches course ID, prints the relevant info on that course
                print("Instructor:",course_list[i][2],)
                print("Current enrolled students:",course_list[i][4])
                retrieving = False
                
                
            elif userinput.lower() == course_list[i][1].lower(): #if user input matches department, prints the relevent info on that course
                print(course_list[i][0])
                retrieving = False

        