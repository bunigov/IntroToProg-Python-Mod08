# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
#   RRoot,1.1.2030,Created starter script
#   RRoot,1.1.2030,Added pseudocode to start assignment 8
#   BUnigov,8.30.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    """Stores data about a product:
    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's price
    methods:
        to_string  prints out product name and price separated by comma
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BUnigov,8.30.2022, Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties
    @property  #getter
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter  #setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:  #is numeric
            raise ProductNameValueCannotBeNumeric

    @property
    def product_price(self):  #getter
        return str(self.__product_price)

    @product_price.setter   #setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except ValueError:  #is not numeric, cannot be converted to float
            raise ProductPriceValueMustBeNumeric

    # -- Methods --
    def to_string(self):
        """ Overrides default str method which prints out information about the object.
            This is the User-friendly name of the function that calls the overridden  ___str___ function.
          :return: references overridden __str___ method
          """
        return self.__str__()

    def __str__(self):  #replacing default str method, will call above one
        """ Overrides default str method which prints out information about the object
          :return: product name value and product price separated by comma
          """
        return self.product_name + ',' + self.product_price

# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes data into a list
    methods: add_data_to_list(product_name, product_price, list):
    changelog: (When,Who,What)
        BUnigov,8.30.2022, Created class.
        BUnigov,8.30.2022, Modified class by adding add_data_to_list method
    """

    @staticmethod
    def add_data_to_list(product_name, product_price, list):
        """ Adds data to a list
          :param product_name: (string) with name of product:
          :param product_price: (string) with the product's price:
          :param list: (list) you want filled with data:
          :return: (list) of rows
          """
        obj = Product(product_name, product_price)
        list.append(obj)
        return list

class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list:
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BUnigov,8.30.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list):
        """ Saves data to file
          :param file_name: (string) filename to save data to (in current directory)
          :param list: (list) list to save to file
          :return: nothing
          """
        print("Option 3 selected - Save Data to File")
        objFile = open(file_name, "w")
        for row in lstOfProductObjects:
            objFile.write(str(row) + "\n")
        objFile.close()
        print("List saved to file \n")

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from file
          :param file_name: (string) filename to read data from (in current directory)
          :return: nothing
          """
        try:
            file = open(file_name, 'r')
            for row in file:
                product_name, product_price = row.split(",")
                Processor.add_data_to_list(product_name.strip(), product_price.strip(), lstOfProductObjects)
            print("Preloading to list from file " + file_name)
        except Exception as e:
            #print(e)
            print("File was not found. Data not loaded. Starting application with no data..") #error handling

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Manages user input and output. Error handling is managed in separate classes.
    methods:
        input_menu_choice()          --> user's menu choice
        input_initial_load_choice()  --> user's initial data pre-load choice
        input_data_to_add_to_list()  -> product name and product price to add
        output_show_menu()
        output_current_data_in_list(list)
        output_show_initial_load_text()

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BUnigov,8.30.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string  user's menu choice
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_initial_load_choice():
        """ Gets the initial choice from the user whether to load data from file
        :return: string  user's initial data preload choice
        """
        initial_load_choice = str(input("Would you like to reload data from file ?   (y/n) ")).strip()
        print()  # Add an extra line for looks
        return initial_load_choice

    @staticmethod
    def input_data_to_add_to_list():
        """  Gets product name and product price values to be added to the list
        :return: (string, string) with product name and product price value user wants added
        """
        product_name = str(input("What is the Product you want to add? - ")).strip().capitalize()
        product_price = str(input("What is Products's price? (Number only, no $) - ")).strip().capitalize()
        print()
        return product_name, product_price

    @staticmethod
    def output_show_menu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Please select from \u001b[1mMenu of Options\u001b[0m
        0) \x1B[4mClear\x1B[0m List
        1) \x1B[4mSee\x1B[0m Current Data in List 
        2) \x1B[4mAdd\x1B[0m Data to List 
        3) \x1B[4mSave\x1B[0m Data to File
        4) \x1B[4mReload\x1B[0m Data from File
        5) \x1B[4mExit\x1B[0m the program
        ''')
        print()  # Add an extra line for looks
        #

    @staticmethod
    def output_current_data_in_list():
        """ Shows the current data in the list
        :param list: (list) of rows
        :return: nothing
        """
        print("Here's the current data in the list ...")
        print("Product Name" + " | " + "Product Price")
        for row in lstOfProductObjects:
            print(row)

    @staticmethod
    def output_show_initial_load_text():
        """  Display instructions to user if they selected to load data from file
        """
        print("Please enter data into file products.txt in the current directory. "
              "Each product name and product price pair must be on its own row. \n" +
              "Please separate the product name and product price with a comma. No spaces please."
              )
        input("When ready, press <Enter> to import data from the file. You will later have the option to clear the list to start with a new list.")
        print("")

# Exceptions / Error Handling  -------------------------------------------- #
class ProductNameValueCannotBeNumeric(Exception):
    """Custom exception error handling class for when product name is numeric  """

    @staticmethod
    def output_product_name_value_cannot_be_numeric_error():
        """  Displays error text when product name that was entered is numeric
             :return: nothing
             """
        print("Error - You must enter a product name value that is not numeric")
        print("Item not added. Try again. \n")

class ProductPriceValueMustBeNumeric(Exception):
    """Custom exception error handling class for when product price is not numeric  """

    @staticmethod
    def output_product_price_value_must_be_numeric_error():
        """  Display error text when the product price that was entered is not numeric
             :return: nothing
             """
        print("Error - You must enter a product price value that is numeric")
        print("Item not added. Try again. \n")

# Main Body of Script  ---------------------------------------------------- #

# Initial Data Load
while(True) :  #runs until valid input received regarding initial load
    initial_load_choice_str = IO.input_initial_load_choice()   #capture initial input whether user wants to load from file to start the app

    if initial_load_choice_str == 'y':
        IO.output_show_initial_load_text()  #provides user instructions pre-load after user decided to load
        FileProcessor.read_data_from_file(strFileName)  #loads file if user decides
        break

    elif initial_load_choice_str == 'n':
        # intentional decision to leave here, not much gain to put in dedicated output function
        print("Per user choice - no data was preloaded. Starting application")
        break

    else:
        # intentional decision to leave here, not much gain to put in dedicated output function
        print("Invalid input. Please try again.")  # error handling if invalid input received
        continue

# Show user current data in the list of product objects
IO.output_current_data_in_list()

# Menu Actions - runs after every selection until user chooses to exit
while(True):  #runs until user exits the application  / continually presents menu of options
    IO.output_show_menu()  # show menu to the user
    menu_choice_str = IO.input_menu_choice()  # Get user's menu option choice

    # User Option 0 - Clear the list
    if menu_choice_str.strip() == '0':
        print("Option 0 selected - Clear List")
        lstOfProductObjects = []
        print("List Cleared")
        IO.output_current_data_in_list()

    # User Option 1 - See current data in list
    elif menu_choice_str.strip() == '1':
        print("Option 1 selected - See Current Data")
        IO.output_current_data_in_list()

    # User Option 2- Add Data to the list
    elif menu_choice_str.strip() == '2':
        print("Option 2 selected - Add Data to List")
        product_name , product_price = IO.input_data_to_add_to_list()  #capture input
        try:
            lstOfProductObjects = Processor.add_data_to_list(product_name, product_price, lstOfProductObjects)
            print("Item added \n")
            IO.output_current_data_in_list()  #show updated list
            continue
        except ProductNameValueCannotBeNumeric:
            ProductNameValueCannotBeNumeric.output_product_name_value_cannot_be_numeric_error()  #error output
        except ProductPriceValueMustBeNumeric:
            ProductPriceValueMustBeNumeric.output_product_price_value_must_be_numeric_error()  #error output

    # User Option 3 - Save current data to file
    elif menu_choice_str.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        IO.output_current_data_in_list()  # show updated list

    # User Option 4 - Reload data to file
    elif menu_choice_str.strip() == '4':
        print("Option 4 selected - Reload Data from File")
        lstOfProductObjects = []  #empty the list just in case
        FileProcessor.read_data_from_file(strFileName)
        IO.output_current_data_in_list()

    # User Option 5 - Exit the Program
    elif menu_choice_str.strip() == '5':
        print("Thank you for using the application!!! Goodbye!! ")
        break