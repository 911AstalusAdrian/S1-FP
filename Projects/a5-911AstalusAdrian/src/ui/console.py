"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from services.service import NumberFunctions


class ui:
    
    def display_list_ui(self, variable):
        """
        UI part for displaying the list of complex numbers
        We use 'variable' in order to use the functions in service
        """
        for number in variable.complex_numbers_list:
            print(number)

    def add_number_ui(self, variable):
        """
        UI part for adding a complex number in the list
        We read the real part and the imaginary part, check if they are integers and then use the add_complex function
        from the class in service
        """
        real_part = input("Give the real part: ")
        imaginary_part = input("Give the imaginary part: ")
        try:
            real_part = int(real_part)
            imaginary_part = int(imaginary_part)
        except ValueError as error:
            print(error)
        variable.add_complex(real_part, imaginary_part)
        print("Number added!")

    def filter_ui(self, variable):
        """
        UI part for filtering the list of complex numbers
        We read the starting and ending indices and check if they are smaller than the length of our list
        We use the filter function of the class in service
        """
        start_position = int(input("Starting position:"))
        end_position = int(input("Ending position:"))
        if start_position > len(variable.complex_numbers_list) or start_position < 1:
            raise ValueError("Invalid starting position!")
        elif end_position > len(variable.complex_numbers_list) or end_position < 1:
            raise ValueError("Invalid ending position")
        else:
            variable.filter_list(start_position, end_position)
            print("List filtered!")

    def print_menu(self):
        """
        The UI menu
        """
        print("\n1. Add a complex number")
        print("2. Display the list of complex numbers")
        print("3. Filter the list")
        print("4. Undo")
        print("0. Exit")

    def start_ui(self):
        variable = NumberFunctions()
        variable.initialise()
        history_list = [] # A list in which we store the previous iterations of our list of complex numbers
        commands_dictionary = {
            '2': self.display_list_ui
        }
        undoable_commands_dictionary = {
            '1': self.add_number_ui,
            '3': self.filter_ui

        }
        done = False
        while not done:
            self.print_menu()
            user_command = input("Type in your command: ")
            if user_command in commands_dictionary:
                try:
                    commands_dictionary[user_command](variable)
                except ValueError as error:
                    print(error)
            elif user_command in undoable_commands_dictionary:
                try:
                    # If a command can be undone, we first add the current list of numbers to the history list
                    # Then we make the changes
                    complex_numbers_tuple = tuple(variable.complex_numbers_list)  # tuples are immovable
                    history_list.append(complex_numbers_tuple)
                    variable.complex_numbers_list = list(variable.complex_numbers_list)
                    undoable_commands_dictionary[user_command](variable)
                except ValueError as ve:
                    print(str(ve))
            elif user_command == '4':
                # For undo, we clear the current list and replace it with the last list from the history list
                # Then we pop the last list of the history list
                # If there are no lists in the history list, there are no actions to be undone
                if len(history_list) != 0:
                    variable.complex_numbers_list.clear()
                    previous_list = list(history_list[len(history_list)-1])
                    for element in previous_list:
                        variable.complex_numbers_list.append(element)
                    history_list.pop()
                    print("Action undone!")
                else:
                    print("No action to be undone")
            elif user_command == '0':
                done = True
            else:
                print("bad command")


complex_numbers_ui = ui()
complex_numbers_ui.start_ui()
