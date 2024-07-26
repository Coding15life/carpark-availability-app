'''
PRG1 Assignment
---------------
Name: Javier Lim Jia Sheng
Class: P08
Student Number: S10241539F
'''

# Import CSV module
import csv

# Global Variables
filepath = "D:\\Year 1\\Programming 1\\Assignment\\carpark-information.csv"
info_list = [] #List with information like parking type, address, and carpark number.
temp_list = []
temp_dict = {}

user_input = None
option_3_exec = False
carpark_avail_list = [] # List with information containing carpark number, total lots and lots avaialble.

lots_not_available = 0
address = None


# Function show_menu(): To show the list of options.
# This function will recursively be called in the program.
def show_menu():
    print("Menu")
    print("====")
    print("[1] Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2] Display All Basement Carparks in 'carpark-information.csv'")
    print("[3] Read Carpark Availability Data File")
    print("[4] Print Total Number of Carparks in the File Read in [3]")
    print("[5] Display Carparks Without Available Lots")
    print("[6] Display Carparks With At Least x% Available Lots")
    print("[7] Diplay Addresses of Carparks With At Least x% Available Lots")
    print("[8] Display All Carpark Within City Provided")
    print("[9] Display Carpark With Highest Number of Lots")
    print("[10] Write Results of [3] and Address To 'carpark-availability-with-address.csv'")
    print("[0] Exit")

# Function option_1(): To display the total number of carparks once data from 'carpark-infomation.csv' has been loaded into the variable 'info_list'.
# This function will execute when option 1 is called.
# It will measure the length of items in the list 'info_list'.
def option_1():
    print()
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'.")
    print("Total Number of carparks in 'carpark-information.csv': {}.".format(len(info_list)))
    print()

# Function option_2(): To display all basement carparks in 'carpark-information.csv'.
# This function essentially gets the items (dictionaries through a for loop).
def option_2():
    bc_count = 0
    # Prints an empty line for ease of viewing of output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    print("{:11}{:20}{}".format("Carpark No", "Carpark Type", "Address"))
    # In the for loop, an if statement checks if the dictionary is a basement carpark by checking if the value of the key "Carpark Type"
    # equates to "BASEMENT CARPARK".
    for dictionary in info_list:
        if dictionary.get("Carpark Type") == "BASEMENT CAR PARK":
            # If it is, it will be displayed as an output.
            print("{:11}{:20}{}".format(dictionary["Carpark Number"], dictionary["Type of Parking System"], dictionary["Address"]))
            # There is a counter that will keep count the number of carparks that are basement carparks.
            bc_count += 1
    # Displays the tota number of carparks which was basement car parks.
    print("Total number: {}".format(bc_count))
    print()

# Function option_3(): To read the carpark availability file.
# This function's primary objective is to read in a file of the the available lots in a carpark.
# These are the steps that it will take to read the file.

def option_3():
    temp_dict = {}

    # Prints an empty line for ease of viewing of output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 3: Read Carpark Availability Data File")
    # 1. It will take in a user input, and store it in a variable called "file_input".
    file_input = input("Enter the file name: ")

    # 2. Tests if program can work
    try:
        # 3. It will open up the file object as parking_data.
        with open("D:\\Year 1\\Programming 1\\Assignment\\" + file_input) as parking_data:
            # 4. It will read the data in the file.
            file_output = parking_data.read()
            # 5. The program will then split the lines of the file using the .split("\n") method. It will be stored in a list named "lines".
            # 6. Given that after reading the data is a success, we need to print out the timestamp. Since timestamp is in the first line, it
            # will have a index of 0. Hence, lines[0] will be stored in the variable named "timestamp".
            lines = file_output.split("\n")
            timestamp = lines[0]
            # 7. Next, the program will split the headers of the file. Since header comes after the timestamp, it will have a index of 1. Hence, lines[1] is stored in info_headers.
            info_headers = lines[1].split(",")
            # 8. A for loop is written to iterate through the list of lines. Since the actual data is from the index of 2 onwards, we can utilise
            # a for loop to loop through each lines and store the data in another list.
            for line in lines[2:]:
                # 9. In the for loop, the line that it is currently at will be split, as they are seperated by commas (with no space). The result will be stored in a list named "temp".
                temp = line.split(",")            
                # 10. A nested for loop is written to iterate through temp.
                for index in range(len(temp)):
                    # 11. This stores the data in a dictionary. The header from "info_headers" will be stored as a key, and the data as a value. This works because they have the same length.
                    temp_dict[info_headers[index]] = temp[index]
                # 12. This dictionary will be appended into the global list, "carpark_avail_list".
                carpark_avail_list.append(temp_dict)
                # 13. The dictionary will be made empty so that other lines of the data can be stored in the "temp" variable.
                temp_dict = {}
            # 14. Since there is a empty string at the end, a pop() function can be utilised to get rid of the value at the end of the list.
            carpark_avail_list.pop()
        print()
        # 15. Timestamp will be printed, as an indicator that the reading of data is successful.
        print(timestamp)
        print()
    # If file produces a FileNotFoundError, it will print a message to alert the user
    # that file is not accessible.
    # A FileNotFoundError occurs when the file does not exist in the current working directory.
    except FileNotFoundError:
        print("File provided does not exist. Please make sure there is no typos.")
    # If file produces a IOError, it will let the user know that it is not readable.
    # A IOError occurs because an input output process failed, such as trying to open the file.
    except IOError:
        print("File is not readable. Please make sure that it has read permission.")

# Function option_4(): To print the total number of carparks in the file previously read in the previous function.
# This function's objective is to simply print the number of carparks read in the file.
# To do this, we can initally set a global variable, option_3_exec, to false.
# This would help us in our check if it was executed. We will check if option_3_exec is True. If it is true, this means that option 3 was executed, hence the program will run normally.

def option_4():
    # Displays a new line for ease of viewing the output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 4: Print Total Number of Carparks in the File Read in [3]")
    # Additionally, a check can be done to make sure that option 3 has been executed.
    if option_3_exec == True:
        # This can be done through the len() function. Len() reads the amount of items in the list. Hence, this function will be suitable for this case.
         print("Total Number of Carparks in the File: {}".format(len(carpark_avail_list)))
    else:
        print("Please run option 3 to use this option.")

# Function option_5(): To count the number of unavailable lots.
# In this funcion, we want to first check if the number of lots in each carpark is equal to 0.

def option_5():
    # Counter to count if lots are not available.
    lots_not_available = 0

    # Displays a new line for ease of viewing the output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 5: Display Carparks Without Available Lots")

    # Again, a check is performed to make sure that option 3 is executed.
    if option_3_exec == True:
        # Since there are a high number of carparks, we can utilise a for loop to loop through the files.
        for lot1 in carpark_avail_list:
            # If it is equal to 0, the program will count it in a variable "lots_not_available".
            if lot1["Lots Available"] == "0":
                lots_not_available += 1
                print("Carpark Number: {}".format(lot1["Carpark Number"]))
    else:
        print("Please run option 3 to use this option.")
    # After counting, the carpark number that is unavailable will be displayed.
    print("Total Number: {}".format(lots_not_available))

# Function option_6(): To display the carpark number, its total lots and availability, and format it in a table.
# This function will be explained in steps.

def option_6():
    # 1. The function declares an empty list called "lots_available".
    lots_available = []

    # Displays a new line for ease of viewing the output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 6: Display Carparks With At Least x% Available Lots")

    # 2. The function checks if option 3 has been executed using an if statement.
    if option_3_exec == True:
        # 3. The function gathers the user input and stores it in a variable called "user_percentage".
        user_percentage = float(input("Enter the percentage required: "))
        # 4. It then prints the header of the table that will be displayed.
        print("{:12}{:12}{:16}{}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))
        # 5. The function then initiates a for loop to iterate through the list with dictionaries "carpark_avail_list". This is the list with the carpark number, lots available, and total lots.
        for lot2 in carpark_avail_list:
            # 6. It will then check if the lots are not empty. If it is true, the percentage of available lots to the total will be calculated.
            if lot2["Lots Available"] != "0":
                percent = (int(lot2["Lots Available"]) / int(lot2["Total Lots"])) * 100
                # 7. An if statement checks if the percentage calculated is more than or equal to the percentage the user gave (user_percentage).
                if percent >= user_percentage:
                    # 8. If it is true, it will append the data in to a string named "lots_available" as a dictionary.
                    lots_available.append({"Carpark Number": lot2["Carpark Number"], "Lots Available": lot2["Lots Available"], "Total Lots": lot2["Total Lots"], "Percentage": round(percent, 1)})
        # 9. A seperate for loop is written to iterate through the lots_available list.
        for dct in lots_available:
            # 10. Through each iteration, it will print out the data through string formatting in table form.
            print("{:12}{:>10}{:>16}{:>12}".format(dct["Carpark Number"], dct["Total Lots"], dct["Lots Available"], dct["Percentage"]))
        # 11. It will also end of by printing the total number of lots which are available.
        print("Total Number: {}".format(len(lots_available)))        
    # 12. However, if there are not true, then a message will be printed to ask the user to run option 3 first before executing this option.        
    else:
        print("Please run option 3 to use this option.")

# Function option_7(): Display the carpark number, total lots, available lots, percentage, and address.
# This function is similar to the above one. However, the difference is that this function will print the address of the carparks that are available and more than or equal to the percentage specified.
# An additional for loop would be required to retrieve the addresses from info_list.
# It will search the list, info_list for a matching carpark and print the relevant addresses.

def option_7():
    # Intitalises a empty list to store lots available.
    lots_available = []

    # Displays a new line for ease of viewing the output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 7: Diplay Addresses of Carparks With At Least x% Available Lots")

    # Checks if option 3 is executed.
    if option_3_exec == True:
        # If option 3 is executed, program will run.
        user_percentage_2 = float(input("Enter the percentage required: "))
        # Prints the table header.
        print("{:12}{:12}{:16}{:12}{}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
        # Iterates through the carpark availability list (carpark number, total lots, and lots available).
        for lot3 in carpark_avail_list:
            # Checks if lots available is not 0.
            if lot3["Lots Available"] != "0":
                # If it is not 0, it will calculate the percentage of lots available.
                percentage = (int(lot3["Lots Available"]) / int(lot3["Total Lots"])) * 100
                # Checks if the percentage is more than or equal to what the user specified in the input.
                if percentage >= user_percentage_2:
                    # If it is, a for loop is initiated to iterate through and get the index.
                    for index2 in range(len(info_list)):
                        # Checks if carpark number matches.
                        if info_list[index2]["Carpark Number"] == lot3["Carpark Number"]:
                            # If so, it appends the relevant information into lots_available list as a dictionary.
                            lots_available.append({"Carpark Number": lot3["Carpark Number"], "Lots Available": lot3["Lots Available"], "Total Lots": lot3["Total Lots"], "Percentage": round(percentage, 1), "Address": info_list[index2]["Address"]})
                            break
        # Loop to retrieve dictionaries from lots_available
        for dct2 in lots_available:
            # Prints out the values
            print("{:<12}{:>10}{:>15}{:>13}  {}".format(dct2["Carpark Number"], dct2["Total Lots"], dct2["Lots Available"], dct2["Percentage"], dct2["Address"]))
        # Prints the total number of carparks using len() function.
        print("Total Number: {}".format(len(lots_available)))
            
    else:
        # Prints error message to run option 3.
        print("Please run option 3 to use this option.")
# Function option_8(): To display the carpark(s) located at where the user has entered.
# This function's primary objective is to search the city / location that the user has entered
# and search within the list for the locations of the carparks within the city.
def option_8():
    # Print an empty line for easier viewing of output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 8: Display All Carpark Within City Provided")

    # Local variables to be used in the function.
    temp_address = None
    city_input = input("Enter the city to search for: ").upper()
    address_count = 0
    carpark_no = []
    carpark_infos = []

    if all(char.isalpha() or char.isspace() for char in city_input):
        #Checks if option 3 is executed.
        if option_3_exec == True:
            # Looping through the info_list (list with carpark number, addresses, type of parking, carpark type, and much more).
            for dictionary_city in info_list:
                # Sets the variable 'temp_address' to the address extracted fron dictionary. 
                temp_address = dictionary_city["Address"]
                # This checks if the city provided by the user is in the address.
                # If it is, it will be appended to the list of carpark numbers 'carpark_no'.
                # It will also be counted in the variable 'address_count', which counts the number of address appended.
                if city_input in temp_address:
                    carpark_no.append(dictionary_city["Carpark Number"])
                    address_count += 1
            # Line to check if address_count is 0.
            # If it is 0, it will print an error message.
            if address_count == 0:
                print("Sorry, there are no carparks in specified city.")
            #Else, the program will continue as per normal.
            else:
                # For loop to iterate through carpark_no (list of carpark numbers that is within city user has entered).
                for number in carpark_no:
                    # Each time the loop is ran, the dictionary is made empty, so that it makes way for the new item.
                    dict_iter = {}
                    # Loop through the list with carpark information (carpark number, addresses, etc.)
                    for item1 in info_list:
                        # If the carpark number matches with the carpark number in the info_list dictionary item, it will add the relevant information to the temporary dictionary.
                        if number == item1["Carpark Number"]:
                            dict_iter["Carpark Number"] = number
                            dict_iter["Address"] = item1["Address"]
                    # Loop through the carpark_avail_list (carpark number, total lots and lots available).
                    for item2 in carpark_avail_list:
                        # If the carpark number matches with the dictionary, the relevant information will be added to the dictionary.
                        if number == item2["Carpark Number"]:
                            dict_iter["Total Lots"] = item2["Total Lots"]
                            dict_iter["Lots Available"] = item2["Lots Available"]
                            # Calculate the percentage of lots available.
                            percentage = round((int(item2["Lots Available"]) / int(item2["Total Lots"])) * 100, 1)
                            # It will also add the percentage to the temporary dictionary.
                            dict_iter["Percentage"] = percentage
                    # The temporary dictionary will be added to the list, 'carpark_infos'.
                    # It will not be a list of dictionaries.
                    carpark_infos.append(dict_iter)
                # This counts the number of dictionaries in the list, which represents the amount of carparks found.
                num_of_carparks = len(carpark_infos)
                # Displaying the table header.
                print("{:15} {:>7} {:>66} {:>15} {:>11}".format("Carpark Number", "Address", "Total Lots", "Lots Available", "Percentage"))

                # To iterate through the list of dictionaries and print out the information for each carpark.
                # If there are no values for a specific field, it will be replaced with "N/A".
                for carparks in carpark_infos: 
                    print("{:15} {:<63} {:<11} {:<15} {}".format(carparks.get("Carpark Number", "N/A"), carparks.get("Address", "N/A"), carparks.get("Total Lots", "N/A"), carparks.get("Lots Available", "N/A"), carparks.get("Percentage", "N/A")))
                print()
                # Prints number of carparks found.
                print("Number of carparks in {}: {}".format(city_input, num_of_carparks))
        else:
           # Prints error message to run option 3.
            print("Please run option 3 to use this option.")
    else:
        print("You have not entered a valid city. Please try again.")

# Function option_9(): Display carpark with the highest amount of lots.
# This function's primary objective to go through the data, and fish out the carpark with the highest amount of lots.
def option_9():
    # Local variables to be used in the function.
    highest_total_lots = 0
    carpark_no_highest = None
    avail_lots = None
    address = None
    carpark_type = None
    carpark_system = None

    # Print an empty line for easier viewing of output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 9: Display Carpark With Highest Number of Lots")

    # For loop to iterate through the carpark_avail_list (the list comprising of carpark numbers, total lots, and lots available.)
    for cp_dict in carpark_avail_list:
        # If the total lots is higher than the highest number of lots (initially will be 0, hence, the current number of
        # total lots will be added first, which will then be replaced by another carpark with the higher amount than this.
        if int(cp_dict["Total Lots"]) > highest_total_lots:
            # Initialises the highest amount of total lots.
            highest_total_lots = int(cp_dict["Total Lots"])
            # Takes note of the carpark number with the highest number of total lots.
            carpark_no_highest = cp_dict["Carpark Number"]
            # It also takes note of the amount of lots available.
            avail_lots = cp_dict["Lots Available"]
    # Loops through the info_list (list containing carpark number, addresses, carpark type, etc.)
    for cp_dict2 in info_list:
        # Checks if the carpark number with the highest amount of total lots matches the carpark number from the dictionary 'cp_dict2'.
        if carpark_no_highest == cp_dict2["Carpark Number"]:
            # If it is, the relevant information will be added to the variables.
            address = cp_dict2["Address"]
            carpark_type = cp_dict2["Carpark Type"]
            carpark_system = cp_dict2["Type of Parking System"]

    # This part prints out the information of the carpark in tabular form.
    print()
    print("{:16}{:16}{:12}{:34}{:24}{}".format("Carpark Number", "Available Lots", "Total Lots", "Address", "Carpark Type", "Carpark System"))
    print(f"{carpark_no_highest:<16}{avail_lots:<16}{highest_total_lots:<11} {address:<33} {carpark_type:<23} {carpark_system}")

# Function option_10(): Adds an additional column (addresses) to the carpark availability file and writes
# it to a new file.
# The function's primary objective is to combine all the information from the carpark availability file
# with another column, addresses, of each carpark.
# We also need to sort the data according to lots available in ascending order.
def option_10():
    # Stores the list containing data of the carpark availability in a new variable, new_carpark_avail.
    new_carpark_avail = carpark_avail_list
    # Intialises a new variable, line_counter, to count the number of lines in the csv file.
    line_counter = 1

    # Another function is written to get the values of the key 'Lots Available', so that they can
    # be sorted out in the later part of the program.
    def get_lots_avail(new_carpark_avail):
        return int(new_carpark_avail.get("Lots Available"))
    
    # Print an empty line for easier viewing of output.
    print()
    # Display the option so that user knows what option is being executed.
    print("Option 10: Write Results of [3] and Address To 'carpark-availability-with-address.csv'")

    # Sorts the new_carpark_avail list based on the lots available in ascending order.
    new_carpark_avail.sort(key=get_lots_avail)

    # Opens a new file to store the information inside.
    with open("carpark-availability-with-addresses.csv", "w", encoding="UTF-8", newline='') as csvfile:
        # This line converts the csv file to a delimited string, which means we can write into it later.
        row = csv.writer(csvfile)
        # Since we have converted it into a delimited string, we can first write to the first row.
        # This row will be the headers.
        row.writerow(["Carpark Number", "Total Lots", "Lots Available", "Address"])
        # Loops through the new carpark availability list to get the data for carpark.
        for data in new_carpark_avail:
            for data2 in info_list:
                # Checks if the dictionary from the new carpark availability list matches the one in info_list.
                # If they do, the information of the carpark will written to the csv file.
                if data["Carpark Number"] == data2["Carpark Number"]:
                    row.writerow([data["Carpark Number"], data["Total Lots"], data["Lots Available"], data2["Address"]])                   
                    # Counts each time a row is appended.
                    line_counter += 1
    # Displays the number of line in the file and file name.
    print(f"Total number of lines in file: {line_counter}.")
    print(f"File written to: carpark-availability-with-addresses.csv")
                    
    
# Reading data from 'carpark-information.csv' file and storing dictionaries of the information in a list.
file = open(filepath, "r")
data = file.read()

# Split each new EOL and store it in a list called "split_lines", with each item in the list representing a line in the file.
split_lines = data.split("\n")


# For loop that will iterate through every line.
# Each line is seperated by commas.
# Hence, we need to use the .split() method to split it and store the results as a nested list in temp_list.

for i in range(len(split_lines)):
    temp_list.append(split_lines[i].split(","))

# Since the first line is a header, it will have an index of 0. We can then store this in a list.
header = temp_list[0]

# For loop to iterate through each data. As the data of interest starts from the index of 1 and more, therefore we can use index slicing to retrieve the data.
# This for loop can be broken down into simple steps.

# 1. The for loop iterates through the data in temp_list. This is the data of the carpark addresses and several other information. Take note that it will retrieve dictionaries in the list.
for line in temp_list[1:]:
    # 2. An empty dictionary is created, in order to temporarily store relevant dictionary data.
    temp_dict = {}
    # 3. A if statement is used to check if i (the index) is lesser than the length of the header (in this case, 3).
    for i in range(len(header)):
        if i < len(line):
            # 4. If it is, it would store the data in a dictionary.
            temp_dict[header[i]] = line[i]
    # 5. After storing each header with its data, the dictionary is appended to the list.
    info_list.append(temp_dict)
# 6. After the whole loop is done, a pop() method is called in order to get rid of the empty string.
info_list.pop()

# While loop to check if the user_input is not equal to 0.
# If it is, and the loop is running, it will exit the loop.
# Else, it will continue.
while True:
    # Function call to show the list of options.
    show_menu()
    # Prompt for user to enter information (can only entered as integer and nothing else.
    user_input = input("Enter your option: ")

    # Try converting user input to integer.
    # Else, it will match the function to the user's option.
    try:
        choice = int(user_input)
        # If the conversion succeeds, it will check if it is within the range of 0 to 10.
        if 0 <= choice <= 10:
            if choice == 0:
                break
            else:
                # If user input matches an option, the relevant function will be executed.
                if choice == 1:
                    option_1()
                    
                elif choice == 2:
                    option_2()
                    
                elif choice == 3:
                    # Ensures that the list is empty.
                    if carpark_avail_list != []:
                        # If it is not, it empties it.
                        carpark_avail_list = []
                        
                    option_3()
                    option_3_exec = True
                    
                elif choice == 4:
                    option_4()

                elif choice == 5:
                    option_5()
    
                elif choice == 6:
                    option_6()
    
                elif choice == 7:
                    option_7()

                elif choice == 8:
                    option_8()
                    
                elif choice == 9:
                    option_9()

                elif choice == 10:
                    option_10()
        # If it is not, an error message will be printed out to ask the user to enter a number between 0 to 10.
        else:
            print("Please enter a number between 0 - 10!")

    # If the conversion fails, it will produce a ValueError. This would subsequently run the except statement, which would print out the message to input a number.
    except ValueError:
        print("You have entered an invalid input! Please enter a number!")
        

