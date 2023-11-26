# Pseudocode:
# FUNCTION get_course_info(course_info, course_number)
#     // This function retrieves course information based on a given course number.
#     RETURN course_info.get(course_number, None)
#
# FUNCTION display_course_info(course_data, course_number)
#     // This function displays the course information.
#     IF course_data EXISTS
#         PRINT "Course number:" followed by course_number
#         TRY
#             PRINT "Room number:" followed by course_data's room_number
#             PRINT "Instructor:" followed by course_data's instructor
#             PRINT "Meeting time:" followed by course_data's meeting_time
#         CATCH KeyError
#             PRINT "Missing information in the course data."
#     ELSE
#         PRINT "Invalid course number. Please enter a valid course number."
#
# FUNCTION main()
#     // Main function to run the program.
#     DEFINE course_info as a dictionary with course details (room number, instructor, meeting time)
#
#     PROMPT user to "Enter a course number:"
#     STORE input in course_number
#
#     CALL get_course_info with course_info and course_number, STORE result in course_data
#
#     CALL display_course_info with course_data and course_number
#
# START main() if the script is the main program


def get_course_info(obj_course_info, str_course_number):
    """
    Get course information for the given course number.

    Args:
        obj_course_info (dict): Dictionary containing course information.
        str_course_number (str): Course number entered by the user.

    Returns:
        dict: Course information (room number, instructor, meeting time).
    """
    return obj_course_info.get(str_course_number, None)


def display_course_info(obj_course_data):
    """
    Display course information.

    Args:
        obj_course_data (dict): Course information.
    """
    if obj_course_data:
        print("Course number:", course_number)
        print("Room number:", obj_course_data["room_number"])
        print("Instructor:", obj_course_data["instructor"])
        print("Meeting time:", obj_course_data["meeting_time"])
    else:
        print("Invalid course number. Please enter a valid course number.")


# Create a dictionary containing course numbers, room numbers, instructors, and meeting times
course_info = {
    "CSC101": {"room_number": "3004", "instructor": "Haynes", "meeting_time": "8:00 a.m."},
    "CSC102": {"room_number": "4501", "instructor": "Alvarado", "meeting_time": "9:00 a.m."},
    "CSC103": {"room_number": "6755", "instructor": "Rich", "meeting_time": "10:00 a.m."},
    "NET110": {"room_number": "1244", "instructor": "Burke", "meeting_time": "11:00 a.m."},
    "COM241": {"room_number": "1411", "instructor": "Lee", "meeting_time": "1:00 p.m."}
}

# Get the course number from the user
course_number = input("Enter a course number: ")

# Get the course information
course_data = get_course_info(course_info, course_number)

# Display the course information
display_course_info(course_data)
