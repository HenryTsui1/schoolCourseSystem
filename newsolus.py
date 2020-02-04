# Name: Henry Tsui
# Student ID: 20105575
# Date: 07/11/2019

import course_change #imported from other modules
import course_info

'''Opening and reading text file line by line, making each line a list.  
Cleansing data and then adding each list into a list.'''
def database(): 
    file = open("courses1.txt", 'r') #opens the courses1.txt file
    lines = file.readlines() #reads file line by line

    course_list = []
    for l in lines:
        course_list.append(l.rstrip('\n').split(", "))
    return course_list #returns the list of lists to call later
            

'''User interface where the user is able to interact with the program'''      
def solusInterface():
    course_list = database()  #local variable
    interface = True
    while interface: 
        print('')
        print('Enter 1 to create a new course')
        print('Enter 2 to update information on a course')
        print('Enter 3 to display course information')

        userinput = input("Enter 4 to retrieve course information\nInput: ")
        if userinput == '1':
            course_change.newCourse(course_list) #parameter of course_list, to call on from other modules
        elif userinput == '2':
            course_change.updateCourse(course_list)
        elif userinput == '3':
            course_info.infoCourse(course_list)
        elif userinput == '4':
            course_info.retrieveCourse(course_list)
        else:
            print("Invalid input") #integer error check
            
      

def main():
    solusInterface()


main() #calls on the main function to run the program