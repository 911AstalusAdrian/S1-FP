
from Exceptions import EntityException, RepositoryException, UndoRedoException
from datetime import date


class UI:
    """
    UI class which contains all the UI functions
    """
    def __init__(self, student_service, assignment_service, grade_service, undo_service):
        self._student_service = student_service
        self._assignment_service = assignment_service
        self._grade_service = grade_service
        self._undo_service = undo_service

    def run(self):
        """
        The 'run' function
        :return: -
        """
        #self._student_service.initialise()
        #self._assignment_service.initialise()
        #self._grade_service.initialise()
        done = False
        menu_dictionary = {
            '1': self.add_student_ui,
            '2': self.add_assignment_ui,
            '3': self.remove_student_ui,
            '4': self.remove_assignment_ui,
            '5': self.update_student_ui,
            '6': self.update_assignment_ui,
            '7': self.list_students_ui,
            '8': self.list_assignments_ui,
            '9': self.assignment_to_student_ui,
            '10': self.assignment_to_group_ui,
            '11': self.grade_assignment_ui,
            '12': self.list_grades_ui,
            '13': self.assignment_top,
            '14': self.late_students,
            '15': self.best_school_situation,
            '16': self.undo,
            '17': self.redo
        }
        while not done:
            self.menu()
            user_input = input("input>  ")
            if user_input in menu_dictionary:
                try:
                    menu_dictionary[user_input]()
                except RepositoryException as re:
                    print(re)
                except EntityException as ee:
                    print(ee)
                except ValueError as ve:
                    print(ve)
                except UndoRedoException as ure:
                    print(ure)
            elif user_input == '0':
                done = True
            else:
                print("Invalid command!")

    def menu(self):
        """
        The menu of the problem. Here are printed all the option a user can choose
        :return: -
        """
        print("1. Add Student\n"
              "2. Add Assignment\n"
              "3. Remove Student\n"
              "4. Remove Assignment\n"
              "5. Update Student\n"
              "6. Update Assignment\n"
              "7. List Students\n"
              "8. List Assignments\n"
              "9. Give Assignment to Student\n"
              "10. Give Assignment to Group\n"
              "11. Grade a Student's Assignment\n"
              "12. List Grades\n"
              "13. Show statistics for an assignment\n"
              "14. Show statistics for late students\n"
              "15. Show the school situation\n"
              "16. Undo\n"
              "17. Redo\n"
              "0. Exit\n")

    def add_student_ui(self):
        """
        UI section for adding a student.
        The user is asked for an input for each of a student's attributes (ID, name, group)
        Using these inputs, we'll try to add the student in the Service class used for Students
        The errors which can appear are caught using the 'except' branch
        :return: -
        """
        student_id = input("Give student ID: ")
        name = input("Give student Name: ")
        group = int(input("Give student group (911 to 917): "))
        try:
            self._student_service.add(student_id, name, group)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def remove_student_ui(self):
        """
        UI section for removing a student.
        Using the user's input, we try to remove an existing Student, making use of his/her specific ID
        The possible errors are caught here
        :return: -
        """
        student_id = input("Give student ID: ")
        try:
            self._student_service.remove(student_id)
            self._grade_service.remove_by_student(student_id)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def update_student_ui(self):
        """
        UI section for updating a student.
        We try to update an existing Student (in this case, updating means changing the name of the student with a specific ID)
        Using the ID given by the user, we try to change the name of the Student with that ID to the new name given by the user
        Errors are caught here
        :return: -
        """
        student_id = input("Give student ID: ")
        name = input("Give new student name: ")
        try:
            self._student_service.update(student_id, name)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def list_students_ui(self):
        """
        UI function for listing all the existent students.
        If there are no students in the students' repository, a message is displayed
        As it's a function that only prints information, there are no errors to be caught
        :return: -
        """
        if len(self._student_service.list_students()) == 0:
            print("There are no students!")
        for student in self._student_service.list_students():
            print(student)

    def remove_assignment_ui(self):
        """
        UI section for removing an assignment.
        We try to remove an assignment based on the user's input
        Any possible errors related to removing an assignment are caught here
        :return: -
        """
        assignment_id = input("Give assignment ID:")
        try:
            self._assignment_service.remove(assignment_id)
            self._grade_service.remove_by_assignment(assignment_id)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def add_assignment_ui(self):
        """
        UI section for adding an assignment.
        Based on the user's input, we try to create an assignment.
        The deadline is a 'date' data type, therefore we need to get the year, the month and the day of the deadline.
        Any errors related to creating and adding an assignment or creating the deadline are caught here
        :return: -
        """
        assignment_id = input("Give assignment ID: ")
        description = input("Give description: ")
        deadline_year = int(input("Give deadline year: "))
        deadline_month = int(input("Give deadline month: "))
        deadline_day = int(input("Give deadline day: "))
        try:
            deadline = date(deadline_year, deadline_month, deadline_day)
            self._assignment_service.add(assignment_id, description, deadline)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)
        except ValueError as ve:
            print(ve)

    def list_assignments_ui(self):
        """
        UI function for listing all the existent assignments.
        If there are no assignments, a message is displayed
        There are no errors to be caught, because we only print data
        :return: -
        """
        if len(self._assignment_service.list_assignments()) == 0:
            print("There are no assignments!")
        for assignment in self._assignment_service.list_assignments():
            print(assignment)

    def update_assignment_ui(self):
        """
        UI function for updating an assignment
        Based on the user's input, we try to update an assignment.
        In this case, updating an assignment means to change its deadline
        Possible errors are caught here
        :return: -
        """
        assignment_id = input("Give assignment ID: ")
        new_year = int(input("Give new year deadline: "))
        new_month = int(input("Give new month deadline: "))
        new_day = int(input("Give new day deadline: "))
        try:
            new_deadline = date(new_year, new_month, new_day)
            self._assignment_service.update(assignment_id, new_deadline)
        except RepositoryException as re:
            print(re)
        except ValueError as ve:
            print(ve)

    def assignment_to_student_ui(self):
        """
        UI function to giving a student an assignment
        In this case, this means giving the student a grade (which is initially 0 - this means the assignment is not graded yet)
        Based on the user input, we add to the student a grade of 0 at the specific assignment
        Possible errors are caught here
        :return: -
        """
        student_id = input("Give student ID: ")
        assignment_id = input("Give assignment ID: ")
        try:
            self._grade_service.add_grade(assignment_id, student_id)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def assignment_to_group_ui(self):
        """
        UI function for giving an entire group of students an assignment
        For every student in the group, a grade of 0 is given at the specific assignment ( 0 means it's not graded yet)
        Possible errors are caught here
        :return:  -
        """
        group = int(input("Give the group of students:"))
        assignment_id = input("Give assignment ID: ")
        try:
            self._grade_service.add_grade_to_group(assignment_id, group)
        except RepositoryException as re:
            print(re)
        except EntityException as ee:
            print(ee)

    def grade_assignment_ui(self):
        student_id = input("Give the student ID: ")
        not_graded_assignments = self._grade_service.show_student_assignments(student_id)
        print('Student ' + student_id + ' has these assignments not graded: ' + str(not_graded_assignments))
        assignment_id = input("Give the assignment ID: ")
        assignment_grade = float(input("Give the grade:"))
        self._grade_service.give_grade(assignment_id, student_id, assignment_grade)

    def list_grades_ui(self):
        """
        UI function for displaying the students' grades
        As it' only a matter of printing, there are no errors to be caught
        :return: -
        """
        if len(self._grade_service.list_grades()) == 0:
            print("There are no grades!")
        for grade in self._grade_service.list_grades():
            print(grade)

    def assignment_top(self):
        assignment_id = input("Give the assignment ID to be verified: ")
        statistic_data = self._grade_service.first_statistic(assignment_id)
        if len(statistic_data) == 0:
            print("There are no statistics for this assignment!")
        else:
            for each_element in statistic_data:
                print(each_element)

    def late_students(self):
        statistic_data = self._grade_service.second_statistic()
        if len(statistic_data) == 0:
            print("There is no data for this statistic!")
        else:
            for each_element in statistic_data:
                print(each_element)

    def best_school_situation(self):
        statistic_data = self._grade_service.third_statistic()
        if len(statistic_data) == 0:
            print("There is no data for this statistic!")
        else:
            for each_element in statistic_data:
                print(each_element)

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()