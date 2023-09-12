import tkinter as tk
from datetime import date
from tkinter import messagebox, simpledialog

from Exceptions import UndoRedoException, RepositoryException, EntityException


class GUI:
    """
      Class used to implement the Graphic User Interface (GUI)
    """

    def __init__(self, student_service, assignment_service, grade_service, undo_service):
        """
        When we initialise the GUI, we need all four services
        :param student_service: Service for the Student entities
        :param assignment_service: Service for the Assignment entities
        :param grade_service: Service for the Grades entities
        :param undo_service: Service for Undo and Redo functionality
        We also create a window using Tkinter. This window is split into 6 rows and 3 columns
        """
        self._student_service = student_service
        self._assignment_service = assignment_service
        self._grade_service = grade_service
        self._undo_service = undo_service
        self._window = tk.Tk()
        for i in range(6):
            self._window.rowconfigure(i, minsize=75, weight=1)
            for j in range(3):
                self._window.columnconfigure(j, minsize=75, weight=1)

    def start(self):
        """
        This function creates all the Buttons which will be placed on the window's 'grid'
        """
        self._window.title("Students Lab Assignment")  # The title of the window
        self._window['bg'] = '#0C0A3E'  # Background colour
        # Each button is placed in the window using 'master', attributed a function using 'command' and put on the grid using .grid()
        button_add_student = tk.Button(master=self._window, text='Add Student', command=self.add_student_gui, bg='#4b2702', fg='white')
        button_add_student.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)  # 'sticky' used to center the button on the grid place, 'padx' and 'pady' to leave some spacing between the buttons
        button_add_assignment = tk.Button(master=self._window, text='Add Assignment', command=self.add_assignment_gui, bg='#4b2702', fg='white')
        button_add_assignment.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        button_remove_student = tk.Button(master=self._window, text='Remove Student', command=self.remove_student_gui, bg='#4b2702', fg='white')
        button_remove_student.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        button_remove_assignment = tk.Button(master=self._window, text='Remove Assignment', command=self.remove_assignment_gui, bg='#7c4103', fg='white')
        button_remove_assignment.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        button_update_student = tk.Button(master=self._window, text='Update Student', command=self.update_student_gui, bg='#7c4103', fg='white')
        button_update_student.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)
        button_update_assignment = tk.Button(master=self._window, text='Update Assignment', command=self.update_assignment_gui, bg='#ae5a05', fg='white')
        button_update_assignment.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)
        button_list_students = tk.Button(master=self._window, text='List Students', command=self.list_students_gui, bg='#7c4103', fg='white')
        button_list_students.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        button_list_assignments = tk.Button(master=self._window, text='List Assignments', command=self.list_assignments_gui, bg='#ae5a05', fg='white')
        button_list_assignments.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        button_assignment_to_student = tk.Button(master=self._window, text='Give Assignment to Student', command=self.assignment_to_student_gui, bg='#ae5a05', fg='white')
        button_assignment_to_student.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        button_assignment_to_group = tk.Button(master=self._window, text='Give Assignment to Group', command=self.assignment_to_group_gui, bg='#e07406')
        button_assignment_to_group.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)
        button_give_grade = tk.Button(master=self._window, text='Grade an Assignment', command=self.grade_assignment_gui, bg='#f98e1f')
        button_give_grade.grid(row=3, column=2, sticky='nsew', padx=10, pady=10)
        button_list_grades = tk.Button(master=self._window, text='List Grades', command=self.list_grades_gui, bg='#e07406')
        button_list_grades.grid(row=2, column=2, sticky='nsew', padx=10, pady=10)
        button_statistic_one = tk.Button(master=self._window, text='Statistic One', command=self.statistic_one_gui, bg='#e07406')
        button_statistic_one.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        button_statistic_two = tk.Button(master=self._window, text='Statistic Two', command=self.statistic_two_gui, bg='#f98e1f')
        button_statistic_two.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
        button_statistic_three = tk.Button(master=self._window, text='Statistic Three', command=self.statistic_three_gui, bg='#faa751')
        button_statistic_three.grid(row=4, column=2, sticky='nsew', padx=10, pady=10)
        button_undo = tk.Button(master=self._window, text='Undo', command=self.undo_gui, bg='#f98e1f')
        button_undo.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
        button_exit = tk.Button(master=self._window, text='Exit', command=self.close_window, bg='#faa751')
        button_exit.grid(row=5, column=1, sticky='nsew', padx=10, pady=10)
        button_redo = tk.Button(master=self._window, text='Redo', command=self.redo_gui, bg='#faa751')
        button_redo.grid(row=5, column=2, sticky='nsew', padx=10, pady=10)
        self._window.mainloop()

    '''
    All the functions below are similar to the ones from the UI file, but adapted to our GUI
    When we need to take the user input, we use:
        'simpledialog.askstring()' when we need a string
        'simpledialog.askinteger()' when we need an integer
        'simpledialog.askfloat()' when we need a float (grading)
    Instead of printing the errors that appear, we use 'messagebox.showwarning', which will put on the screen an error message
    In the case of the GUI, another type of error can appear, the ValueError, which appears when no data is introduced
        - this error is also caught  
    For the 'list' functionalities, the entities from the lists have been converted into strings 
        Then, these lists will be displayed into a new window, in a label 
    '''

    def add_student_gui(self):
        student_id = simpledialog.askstring(title="Add Student", prompt="Give the Student ID")
        name = simpledialog.askstring(title="Add Student", prompt="Give the Student Name")
        group = simpledialog.askinteger(title="Add Student", prompt="Give the Student Group (int between 911 and 917)")
        try:
            self._student_service.add(student_id, name, group)
            messagebox.showinfo(message="Student added!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def add_assignment_gui(self):
        assignment_id = simpledialog.askstring(title="Add Assignment", prompt="Give the Assignment ID: ")
        description = simpledialog.askstring(title="Add Assignment", prompt="Give the Assignment Description: ")
        deadline_year = simpledialog.askinteger(title="Add Assignment", prompt="Give the Assignment Deadline year: ")
        deadline_month = simpledialog.askinteger(title="Add Assignment", prompt="Give the Assignment Deadline month: ")
        deadline_day = simpledialog.askinteger(title="Add Assignment", prompt="Give the Assignment Deadline day: ")
        try:
            deadline = date(deadline_year, deadline_month, deadline_day)
            self._assignment_service.add(assignment_id, description, deadline)
            messagebox.showinfo(message="Assignment added!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))
        except ValueError as ve:
            messagebox.showwarning(message=str(ve))

    def remove_student_gui(self):
        student_id = simpledialog.askstring(title="Student Removal", prompt="The ID of the Student to be removed: ")
        try:
            self._student_service.remove(student_id)
            self._grade_service.remove_by_student(student_id)
            messagebox.showinfo(message="Student (and corresponding grades) removed!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def remove_assignment_gui(self):
        assignment_id = simpledialog.askstring(title="Assignment removal", prompt="Give the ID of the Assignment to be removed: ")
        try:
            self._assignment_service.remove(assignment_id)
            self._grade_service.remove_by_assignment(assignment_id)
            messagebox.showinfo(message="Assignment (and corresponding grades) removed!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def update_student_gui(self):
        student_id = simpledialog.askstring(title="Updating Student", prompt="Give Student ID: ")
        name = simpledialog.askstring(title="Updating Student", prompt="Give new Student Name: ")
        try:
            self._student_service.update(student_id, name)
            messagebox.showinfo(message="Student updated!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def update_assignment_gui(self):
        assignment_id = simpledialog.askstring(title="Updating Assignment", prompt="Give Assignment ID: ")
        new_year = simpledialog.askinteger(title="Updating Assignment", prompt="Give new Deadline year: ")
        new_month = simpledialog.askinteger(title="Updating Assignment", prompt="Give new Deadline month: ")
        new_day = simpledialog.askinteger(title="Updating Assignment", prompt="Give new Deadline day: ")
        try:
            new_deadline = date(new_year, new_month, new_day)
            self._assignment_service.update(assignment_id, new_deadline)
            messagebox.showinfo(message="Assignment updated!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))
        except ValueError as ve:
            messagebox.showwarning(message=str(ve))

    def list_students_gui(self):
        list_of_students = self._student_service.list_students()
        list_of_students = [str(student) for student in list_of_students]
        list_of_students = '\n\n'.join(list_of_students)
        new_window = tk.Toplevel(self._window)
        new_window.title("List of Students")
        new_window.geometry('500x500')
        tk.Label(new_window, text=str(list_of_students)).pack()

    def list_assignments_gui(self):
        list_of_assignments = self._assignment_service.list_assignments()
        list_of_assignments = '\n\n'.join(str(assignment) for assignment in list_of_assignments)
        new_window = tk.Toplevel(self._window)
        new_window.title("List of Assignments")
        new_window.geometry('500x300')
        tk.Label(new_window, text=str(list_of_assignments)).pack()

    def assignment_to_student_gui(self):
        student_id = simpledialog.askstring(title="Assignment to Student", prompt="Give the Student ID: ")
        assignment_id = simpledialog.askstring(title="Assignment to Student", prompt="Give the Assignment ID: ")
        try:
            self._grade_service.add_grade(assignment_id, student_id)
            messagebox.showinfo(message="Student now has this Assignment")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def assignment_to_group_gui(self):
        assignment_id = simpledialog.askstring(title="Assignment to Group", prompt="Give the Assignment ID: ")
        group = simpledialog.askinteger(title="Assignment to Group", prompt="Give the Group: ")
        try:
            self._grade_service.add_grade_to_group(assignment_id, group)
            messagebox.showinfo(message="Assignment given to all Students from the Group!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def grade_assignment_gui(self):
        student_id = simpledialog.askstring(title="Grade Assignment", prompt="Give the Student ID: ")
        not_graded_assignments = self._grade_service.show_student_assignments(student_id)
        message = 'Ungraded Assignments: ' + str(not_graded_assignments)
        assignment_id = simpledialog.askstring(title="Grade Assignment", prompt=message)
        assignment_grade = simpledialog.askfloat(title="Grade Assignment", prompt="Give the grade (float): ")
        try:
            self._grade_service.give_grade(assignment_id, student_id, assignment_grade)
            messagebox.showinfo(message="Grade Added!")
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))
        except EntityException as ee:
            messagebox.showwarning(message=str(ee))
        except TypeError as te:
            messagebox.showwarning(message=str(te))

    def list_grades_gui(self):
        list_of_grades = self._grade_service.list_grades()
        list_of_grades = '\n\n'.join(str(grade) for grade in list_of_grades)
        new_window = tk.Toplevel(self._window)
        new_window.title("List of Grades")
        new_window.geometry("500x800")
        tk.Label(new_window, text=str(list_of_grades)).pack()

    def statistic_one_gui(self):
        assignment_id = simpledialog.askstring(title="Statistic One Input", prompt="Give the Assignment ID")
        try:
            statistic_result = self._grade_service.first_statistic(assignment_id)
            if len(statistic_result) == 0:
                messagebox.showinfo(message="There are no Grades for this Assignment!")
            else:
                statistic_result = '\n\n'.join(str(statistic_element) for statistic_element in statistic_result)
                statistic_window = tk.Toplevel(self._window)
                statistic_window.geometry('500x500')
                statistic_window.title("Statistic for the required Assignment")
                tk.Label(statistic_window, text=str(statistic_result)).pack()
        except RepositoryException as re:
            messagebox.showwarning(message=str(re))

    def statistic_two_gui(self):
        second_statistic_results = self._grade_service.second_statistic()
        if len(second_statistic_results) == 0:
            messagebox.showinfo(message="There are no late Students!")
        else:
            second_statistic_results = '\n\n'.join(str(statistic_element) for statistic_element in second_statistic_results)
            new_window = tk.Toplevel(self._window)
            new_window.title("Statistic for Late Students")
            new_window.geometry("500x500")
            tk.Label(new_window, text=str(second_statistic_results)).pack()

    def statistic_three_gui(self):
        third_statistic_results = self._grade_service.third_statistic()
        if len(third_statistic_results) == 0:
            messagebox.showinfo(message='There are no existent students!')
        else:
            third_statistic_results = "\n\n".join(str(statistic_element) for statistic_element in third_statistic_results)
            new_window = tk.Toplevel(self._window)
            new_window.title("Statistic for School Situation")
            new_window.geometry('500x300')
            tk.Label(new_window, text=str(third_statistic_results)).pack()

    def undo_gui(self):
        try:
            self._undo_service.undo()
            messagebox.showinfo(message="Action Undone!")
        except UndoRedoException as ure:
            messagebox.showinfo(message=str(ure))

    def redo_gui(self):
        try:
            self._undo_service.redo()
            messagebox.showinfo(message="Action Redone!")
        except UndoRedoException as ure:
            messagebox.showinfo(message=str(ure))

    # Function used to exit the GUI

    def close_window(self):
        self._window.destroy()
