"""This program emulates a simple expense tracking program. It employs various functions
to add expenses to a list, save those expenses, and perform a certain number of 
operations on those expenses (total cost, matching of categories, etc.)

Task: Your task is to complete the implementation of the code and make sure that matches
the requirements set in the assignment's prompt.
First, you will have to make your code identifiable by setting the following information.

******************************************************
Name: RUTAREMARA Wilson
Andrew ID: wrutarem
Semester: Summer 2023
Course: Introduction to Python
Last modified: <the last modification date of your code>
******************************************************

"""

import os
import sys
from typing import Tuple

## Declare a global variable to contain all the expenses processed in the program
expenses = []


class BadInputException(Exception):
   """Vanilla exception class used for testing"""
   pass

def add_expense(category: str, amount: float):
   """Appends an expense to the `expenses` variable.

   Args:
      - category: the name of the category of the expense. type: string
      - amount: the amount of the expense. type: float

   Returns: None

   Raises: 
      - ValueError: if the input is not valid.
   """
   # statement to use the global expenses object
   global expenses
   # Python is not a strong typed language meaning that you have
   # no certainty over the type of data that you receive in your
   # calls. So it is good practice to verify that the type of the input is
   # okay.

   #TODO: Verify that the category variable contains at least three characters

   #TODO: Verify that the amount variable is a floating value strictly greater than zero.
   # You can use the float function (https://docs.python.org/3/library/functions.html#float)

   #TODO: If any of the two values is not valid, raise a BadInputException with the message "Invalid input"
   # now that you have confirmed that the values are valid, you can add them to the list
   #TODO: Append a tuple (category, amount) to the `expenses` list
   if len(category) < 3:
      raise BadInputException("Invalid input")
   try:
        amount = float(amount)
        if amount <= 0:
            raise BadInputException("Invalid input")
   except ValueError:
        raise BadInputException("Invalid input")
    
   expenses.append((category, amount))
   dump_expenses()
   print("Expense added successfully!")


#Now  let us add the values to the list

def dump_expenses(file_path = 'expenses.txt'):
   """Dumps the content of the list to a file

      Returns: None

      Args:
         - file_path: the location of the output file. type 'string'
   """
   global expenses
   #TODO: Open the file by overriding its content first (https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
   #TODO: For each tuple in the `expenses`' list, write a line in the file in the CSV format (e.g., Clothes,10.05)
   # Use a precision of 2 decimal points for the amount.

   with open(file_path,'w',encoding="utf-8") as file:
# For each tuple in the `expenses` list, write a line in the file in the CSV format (e.g., Clothes,10.05)
      for expense in expenses:
         category, amount = expense
         file.write(f"{category},{amount:.3f}\n")

def read_expenses(file_path = 'expenses.txt'):
   """Reads the expenses from a file and saves it as a tuple into the expenses list

   Returns: None

   Args:
      - file_path: the path to the input file. type: string
   """
   global expenses
   #TODO:Read the file, and based on the output format used in `dump_expenses`, load the content into
   # the list. If the file does not exist, safely return from the function.
   # Refer to https://docs.python.org/3/tutorial/errors.html for more guidance on how to handle
   # errors in Python and https://docs.python.org/3/tutorial/inputoutput.html for access to the file.

   if not os.path.exists(file_path):
      return
   with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                category, amount = line.split(',')
                amount = float(amount)
                expenses.append((category, amount))


def get_expenses_by_category(category):
   """Returns a list of all the expenses that matches the category passed as argument.

   Args:
      - category: the category to match the expenses against.

   Returns:
      A list of expenses matching the set criteria
   """
   global expenses
   #TODO:Return a list of tuple of expenses of which the category is equal to the parameter

   matching_expenses = []

   for expense in expenses:
      expense_category, _ = expense
      if expense_category == category:
         matching_expenses.append(expense)
   return matching_expenses

def calculate_total_expenses():
   """Returns the total of the amounts recorded as expenses.

   Args: None

   Returns: the total amount of the expenses

   """
   global expenses
   #TODO: compute and return the total of the amounts in the list.

   total = sum(amount for _, amount in expenses)
   return total

def get_menu_action() -> int:
   """This function shows the menu and interprets the action to be done
   by the user.

   Args: None
   Returns: the user's selection.

   """
   #TODO: Change the loop's condition so that the user keeps being prompted
   # until their input is valid (i.e. in [1, 4])
   while True:
      print('Menu:')
      print('1. Add an expense')
      print('2. View expenses by category')
      print('3. Calculate total expenses')
      print('4. Exit')

      try:
         choice = int(input('Enter your choice: '))
         if choice in [1, 2, 3, 4]:
            return choice
         else:
            raise ValueError()
      except ValueError:
         print("Invalid Choice, Pay attention to options provided above")

      #TODO: Modify the next line to have the `choice` variable store the selection
      ## of the user
   #    choice = None
   # return choice

def print_expense(expense: Tuple[str, float]) -> str:
   """Prints an instance of an expense.

   Args:
      - expense: the expense to be displayed. type: a tuple of a string and a floating point number

   Returns:
      - The string representation to be displayed
   """
   #TODO:Produce an output such that the line starts with a | and ends with the same |.
   # the category should be output by using 10 characters, left-aligned, space-filled.
   # the amount is preceded by a $ sign, and occupies as well 10 characters, left-aligned, space filled.
   # here space filled means that if there is less than 10 characters, you should fill the
   # line with spaces. Extra characters can be truncated. Use 2 decimal positions for the amount.
   # Below two examples

   # in: (Clothes,5.5525) -> out: |Clothes   |$5.55     |
   # in: (House Materials,2424.69) -> out: |House Mate|$2424.69  |

   category, amount = expense
   formatted_line = "| {:<10s} | ${:>8.2f} |".format(category[:10], amount)
   return formatted_line

if __name__ == "__main__":
   #TODO: Read the expenses, if file exists, into the 'expenses' list
   read_expenses()
   
   ## Retrieve the user's choice
   while True:
      command = get_menu_action()
      if command == 1:
         category = input('Expense Category: ')
         amount = input('Expense Amount: ')
         add_expense(category, amount)

      elif command == 2: 
         
         category = input('Expense Category: ')
         matching_expenses = get_expenses_by_category(category)
         print(f"Expenses for Category: {category}")
         print('|Category    | Amount   |')
         print('***********************')
         for expense in matching_expenses:
            print(print_expense(expense))
      elif command == 3:
         total = calculate_total_expenses()
         formatted_total = "{:.2f}".format(total)
         print("Total expenses: $" + formatted_total)
         # print(f'Total expenses is: {total:.2f}')
      elif command == 4:
         #TODO: Save the list of expenses into a file for future use
         #TODO: change the next statement to exit the program gracefully
         dump_expenses()
         print("Exiting the Expense Tracker Application...")
         sys.exit()

      
      else:
         raise ValueError('Invalid command entered')