# design_project.py
# ENDG 233 F25
# Nate Olson, Ruald James
# Pairs L01 - 26
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

### imports
import numpy as np
import matplotlib.pyplot as plt

from user_csv import read_csv, write_csv
from analysis import *


### functions
def menu_options1()	->	str:
	while True:
		print("Please select one of the folowing options:")
		print("Menu Options:")
		print("1. Compare 2 Countries")
		print("2. Single Country Analysis")
		print("3. Exit Program")
		user_choice = input("Please select an option (1-3): ")
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")

def compare_countries_region_menu() -> list:
	while True:
		print("Please select 2 countries")
		user_country1 = input("Please select the 1st country: ")
		user_country2 = input("Please select the 2nd country: ")
		
		country_data = np.array(read_csv("country_data.csv", False))
		flag = 0
		for i in country_data:
			if i[0] == user_country1:
				flag += 1
			if i[0] == user_country2:
				flag += 1
			if flag == 2:
				break
		if flag == 2:
			return [user_country1, user_country2]
		else:
			print("Invalid input. Please provide 2 valid inputs")

def compare_countries_inner_menu() -> str:

	while True:
		print("Country Comparison Options:")
		print("1. Compare Population Densities")
		print("2. Compare Endangered Species")
		print("3. Return to Main Menu")
		user_choice = input("Please select an option (1-3): ")
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")

def print_densities_comparison(user_countries: list) -> None:
	country1 = user_countries[0]
	country2 = user_countries[1]

	output = compare_population_densities(country1, country2)
	print(format_list_to_string(output))

def print_endangered_species(user_countries: list) -> None:
	country1 = user_countries[0]
	country2 = user_countries[1]

	output = compare_endangered_species(country1, country2)
	print(format_list_to_string(output))

def single_country_region() -> str:
	pass
	while True:
		user_country = input("Please select a country: ")

		country_data = np.array(read_csv("country_data.csv", False))
		for i in country_data:
			if user_country == i[0]:
				return user_country
			else:
				print("Invalid input. Please input a valid country")

def single_country_inner_menu() -> str:
	while True:
		print("Single Country Data Options:")
		print("1. Maximum Population")
		print("2. Mean Population")
		print("3. Return to Main Menu")
		user_choice = input("Please select an option (1-3): ")
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")

def print_max_pop(country) -> None:
	max_pop = maximum_population(country)
	print(f"The maximum population of {country} is {max_pop:.0f}.")

def print_mean_pop(country) -> None:
	mean_pop = mean_population(country)
	print(f"The maximum population of {country} is {mean_pop:.0f}.")

		



### testing
def main() -> None:
	print("Welcome to our app")

	while True:
		outer_user_choice = menu_options1()
		if outer_user_choice == "1":
			while True:
				country_list = compare_countries_region_menu()
				inner_user_choice = compare_countries_inner_menu()
				if inner_user_choice == "1":
					print_densities_comparison()
				elif inner_user_choice == "2":
					print_endangered_species()
				else:
					break

		elif outer_user_choice == "2":
			while True:
				user_country = single_country_region()
				inner_user_choice = single_country_region()
				if inner_user_choice == "1":
					print_max_pop()
				elif inner_user_choice == "2":
					print_mean_pop()
				else:
					break
		else:
			break



	print("Thank you for using our app")
	return None

if __name__ == "__main__":
	main()
