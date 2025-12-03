# design_project.py
# ENDG 233 F25
# Nate Olson, Ruald James
# Pairs L01 - 26
# A set of functions for building the terminal menu in main.py

### imports
import numpy as np
import matplotlib.pyplot as plt

from user_csv import read_csv, write_csv

from analysis import compare_population_densities, \
					 compare_endangered_species, \
					 population_density_per_year, \
					 endangered_species_per_capita, \
					 maximum_population, \
					 mean_population, \
					 format_array_to_string

from plot import comparison_bar_plot


### functions
def menu_options1()	->	str:
	''' Prints the main menu options and asks user for menu selection.
	Parameters:
		None
	Returns: 
		str: The user's menu selction as a string
	'''

	while True: 	# loop until valid input
		# Printing out menu options
		print("Please select one of the folowing Menu options:") 
		print("\t1. Compare 2 Countries")
		print("\t2. Single Country Analysis")
		print("\t3. Exit Program")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()
		if user_choice in ['1', '2', '3']: # If vaild input
			return user_choice # return user input
		else: # If invalid input
			print("Invalid input. Please try again.") # Print error message
			print()

def compare_countries_region_menu() -> list:
	''' Asks and grabs the user for the 2 countries they want to compare.
	Parameters:
		None
	Returns:
		list: A list containing the 2 countries the user selected
	'''

	while True: # loop until valid input
		
		# Asks user and grabs the 2 countries they want to compare
		print("Please select 2 countries")
		user_country1 = input("Please select the 1st country: ").title()
		user_country2 = input("Please select the 2nd country: ").title()
		print()
		
		country_data = np.array(read_csv("country_data.csv", False)) # reads country data and saves it as a np array
		flag = 0 # Initializes a flag for validation

		for i in country_data: # loops through country data to check if both countries are valid
			if i[0] == user_country1: # If first country is valid add 1 to flag
				flag += 1
			if i[0] == user_country2: # If second country is valid add 1 to flag
				flag += 1
			if flag == 2: # If both countries are valid, break
				break
		if flag == 2: # If both countries are valid, return them as a list
			return [user_country1, user_country2]
		else: # If either country is invalid, print error message and loop again
			print("Invalid input. Please provide 2 valid inputs")
			print()

def compare_countries_inner_menu() -> str:
	''' Asks user for what type of comparison they want to do between 2 countries.
	Parameters:
		None
	Returns:
		str: The user's menu selction as a string
	'''
	while True: # loop until valid input
		# Printing out menu options
		print("Country Comparison Options:")
		print("\t1. Compare Population Densities")
		print("\t2. Compare Endangered Species")
		print("\t3. Return to Main Menu")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()
		if user_choice in ['1', '2', '3']: # If user choice is valid
			return user_choice # return user choice
		else: # If user choice is invalid
			print("Invalid input. Please try again.") # Print error message
			print()

def print_densities_comparison(user_countries: list) -> np.array:
	'''Calculates and prints the population density comparison between 2 countries
		and returns the data as an array.
	Parameters:
		user_countries (list): A list containing the 2 countries to compare
	Returns:
		np.array: An array containing the population density comparison data
	'''

	# Stores the 2 countries to compare from the user input list
	country1 = user_countries[0]
	country2 = user_countries[1]

	output = compare_population_densities(country1, country2) # Calls the comparison function and stores the output
	print(format_array_to_string(output)) # Prints the output in a formatted string using the format function
	return output # Returns the data array for later use

def print_endangered_species(user_countries: list) -> np.array:
	'''Calculates and prints the endangered species comparison between 2 countries
		and returns the data as an array.
	Parameters:
		user_countries (list): A list containing the 2 countries to compare
	Returns:
		np.array: An array containing the endangered species comparison data
	'''
	# Stores the 2 countries to compare from the user input list
	country1 = user_countries[0] 
	country2 = user_countries[1]

	output = compare_endangered_species(country1, country2) # Calls the comparison function and stores the output
	print(format_array_to_string(output)) # Prints the output in a formatted string using the format function
	return output # Returns the data array for later use

def want_graph(data: np.array) -> None:
	''' Asks user if they want to show or save a graph of the data provided.
	Parameters:
		data (np.array): The data to be graphed
	Returns:
		None
	'''
	# Asks user if they want to show and save the graph
	graph_show = input("Do you want to show graph(T/F)? (*Note: the program will stop until window is closed*) ")
	graph_save = input("Do you want to save graph(T/F)? ")
	print()
	# Converts user input to boolean values
	graph_show = (True if graph_show == "T" else False)
	graph_save = (True if graph_save == "T" else False)


	if graph_save: # If user wants to save the graph
		name = "user_graph.png" # Asks user for filename
		comparison_bar_plot(data, graph_show, graph_save, name) # Calls the plotting function with filename
	else:
		comparison_bar_plot(data, graph_show, graph_save) # Calls the plotting function without filename
	
def want_save(data: np.array) -> None:
	''' Asks the user if they want to save the data as a csv file
		and saves and writes the data if they do.
	Parameters:
		data (np.array): The data to be saved
	Returns:
		None
	'''

	want_save = input("Do you want to save your data as a csv(T/F)? ") # Asks user if they want to save the data
	want_save = (True if want_save == "T" else False) # Converts user input to boolean value

	if want_save: # If user doeas want to save the data
		name = "user_built_csv.csv"
		write_csv(name, data.tolist(), False) # Writes the data to a csv file with the given filename
	return None

def single_country_region() -> str:
	''' Asks the user for a single country that they want to data for.
	Parameters:
		None
	Returns:
		str: The country the user selected
	'''
	while True: # loop until valid input
		user_country = input("Please select a country: ").title() # Asks user for country, and capitalizes the first letter

		country_data = np.array(read_csv("country_data.csv", False)) # reads country data and saves it as a np array
		for i in country_data: # loops through country data to check if country is valid
			if user_country == i[0]: # If country is valid
				return user_country # return the country
		else: # If country is invalid
			print()
			print("Invalid input. Please input a valid country") # Print error message
			print()

def single_country_inner_menu() -> str: 
	''' Asks the user for what type of data they want for a single country
	Parameters:
		None
	Returns:
		str: The user's menu selction as a string
	'''
	while True: # loop until valid input
		# Printing out menu options
		print("Single Country Data Options:")
		print("\t1. Maximum Population")
		print("\t2. Mean Population")
		print("\t3. Return to Main Menu")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()

		if user_choice in ['1', '2', '3']: # If user choice is valid
			return user_choice # return user choice
		else: # If user choice is invalid
			print("Invalid input. Please try again.") # Print error message
			print() 

def print_max_pop(country: str) -> None:
	"""Prints the maximum population of a given country from 2000 - 2020.
	Parameters:
		country (str): the country to find the max population of 
	"""

	max_pop = maximum_population(country) # Calls the maximum population function saves it to variable
	print(f"The maximum population of {country} is {max_pop:.0f}.") # Prints the maximum population

def print_mean_pop(country) -> None:
	"""Prints the mean population of a given country from 2000 - 2020.
	Parameters:
		country (str): the country to find the mean population of
	"""
	mean_pop = mean_population(country) # Calls the mean population function saves it to variable
	print(f"The mean population of {country} is {mean_pop:.0f}.") # Prints the mean population

### testing
def main() -> None:
	"""Runs the main terminal loop."""

	print("Welcome to our app") # Print welcome message
	print()

	while True: # Main loop, loop until user wants to exit
		# Grabs user menu choice from main menu
		outer_user_choice = menu_options1()
		if outer_user_choice == "1": # If user wants to compare 2 countries
			while True: # Inner loop for comparing countries, loop until user wants to return to main menu
				inner_user_choice = compare_countries_inner_menu() # Grabs user menu choice from compare countries menu
				if inner_user_choice == "3": # If user wants to return to main menu
					break # break inner loop
				else:

					country_list = compare_countries_region_menu() # Grabs the 2 countries to compare from user

					if inner_user_choice == "1": # If user wants to compare population densities
						data = print_densities_comparison(country_list) # Calls the print densities comparison function and saves the data
						want_save(data) # Asks user if they want to save the data
					elif inner_user_choice == "2":
						data = print_endangered_species(country_list) # Calls the print endangered species function and saves the data
						want_graph(data) # Asks user if they want to graph data
						want_save(data) # Asks user if they want to save the data


		elif outer_user_choice == "2": # If user wants single country analysis
			while True: # Inner loop for single country analysis, loop until user wants to return to main menu

				inner_user_choice = single_country_inner_menu() # Grabs user menu choice from single country analysis menu
				if inner_user_choice == "3": # If user wants to return to main menu
					break # break inner loop
				else:

					user_country = single_country_region() # Grabs the country to analyze from user

					if inner_user_choice == "1": # If user wants maximum population
						print_max_pop(user_country) # Calls the print maximum population function
					elif inner_user_choice == "2": # If user wants mean population
						print_mean_pop(user_country) # Calls the print mean population function
		else: # If user wants to exit program
			break # break main loop

	print("Thank you for using our app") # Print exit message
	return None

if __name__ == "__main__":
	main()
