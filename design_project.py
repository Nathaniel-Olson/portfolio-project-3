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
	''''''

	while True:
		print("Please select one of the folowing Menu options:")
		print("\t1. Compare 2 Countries")
		print("\t2. Single Country Analysis")
		print("\t3. Exit Program")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")
			print()

def compare_countries_region_menu() -> list:
	while True:
		print("Please select 2 countries")
		user_country1 = input("Please select the 1st country: ").capitalize()
		user_country2 = input("Please select the 2nd country: ").capitalize()
		print()
		
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
			print()

def compare_countries_inner_menu() -> str:
	while True:
		print("Country Comparison Options:")
		print("\t1. Compare Population Densities")
		print("\t2. Compare Endangered Species")
		print("\t3. Return to Main Menu")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")
			print()

def print_densities_comparison(user_countries: list) -> np.array:
	country1 = user_countries[0]
	country2 = user_countries[1]

	output = compare_population_densities(country1, country2)
	print(format_array_to_string(output))
	return output

def print_endangered_species(user_countries: list) -> np.array:
	country1 = user_countries[0]
	country2 = user_countries[1]

	output = compare_endangered_species(country1, country2)
	print(format_array_to_string(output))
	return output

def want_graph(data: np.array) -> None:
	graph_show = input("Do you want to show graph(T/F)? (*Note: the program will stop until window is closed*) ")
	graph_save = input("Do you want to save graph(T/F)? ")
	print()
	graph_show = (True if graph_show == "T" else False)
	graph_save = (True if graph_save == "T" else False)

	if graph_save:
		name = input("Please input the filename to save as (dont include .png): ")
		comparison_bar_plot(data, graph_show, graph_save, filename = f"{name}.png")
	else:
		comparison_bar_plot(data, graph_show, graph_save)
	
def want_save(data: np.array) -> None:
	want_save = input("Do you want to save your data as a csv(T/F)? ")
	want_save = (True if want_save == "T" else False)
	if want_save:
		while True:
			name = input("Please input the filename to save as (dont include .csv): ")
			if name == "country_data" or name == "population_data" or name == "threatened_species":
				print("Filename in use. Please Try Again.")
				print()
			else:
				break
		write_csv(f"{name}.csv", data.tolist(), False)
	return None

def single_country_region() -> str:
	while True:
		user_country = input("Please select a country: ").capitalize()

		country_data = np.array(read_csv("country_data.csv", False))
		for i in country_data:
			if user_country == i[0]:
				return user_country
		else:
			print()
			print("Invalid input. Please input a valid country")
			print()

def single_country_inner_menu() -> str:
	while True:
		print("Single Country Data Options:")
		print("\t1. Maximum Population")
		print("\t2. Mean Population")
		print("\t3. Return to Main Menu")
		print()
		user_choice = input("Please select an option (1-3): ")
		print()
		if user_choice in ['1', '2', '3']:
			return user_choice
		else:
			print("Invalid input. Please try again.")
			print()

def print_max_pop(country: str) -> None:
	"""Prints the maximum population of a given country from 2000 - 2020.
	Parameters:
		country (str): the country to find the max population of 
	"""
	max_pop = maximum_population(country)
	print(f"The maximum population of {country} is {max_pop:.0f}.")

def print_mean_pop(country) -> None:
	"""Prints the mean population of a given country from 2000 - 2020.
	Parameters:
		country (str): the country to find the mean population of
	"""
	mean_pop = mean_population(country)
	print(f"The mean population of {country} is {mean_pop:.0f}.")

### testing
def main() -> None:
	print("Welcome to our app")

	while True:
		outer_user_choice = menu_options1()
		if outer_user_choice == "1":
			while True:
				inner_user_choice = compare_countries_inner_menu()
				if inner_user_choice == "3":
					break
				else:

					country_list = compare_countries_region_menu()

					if inner_user_choice == "1":
						data = print_densities_comparison(country_list)
						want_save(data)
					elif inner_user_choice == "2":
						data = print_endangered_species(country_list)
						want_graph(data)
						want_save(data)


		elif outer_user_choice == "2":
			while True:
				inner_user_choice = single_country_inner_menu()
				if inner_user_choice == "3":
					break
				else:

					user_country = single_country_region()

					if inner_user_choice == "1":
						print_max_pop(user_country)
					elif inner_user_choice == "2":
						print_mean_pop(user_country)
		else:
			break

	print("Thank you for using our app")
	return None

if __name__ == "__main__":
	main()
