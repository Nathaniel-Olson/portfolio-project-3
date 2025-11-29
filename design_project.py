# design_project.py
# ENDG 233 F25
# Nate Olson, Ruald James
# Pairs L01 -26
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

### imports
import numpy as np
import matplotlib.pyplot as plt

from user_csv import read_csv, write_csv

### functions
def format_list_to_string(data: list[list]) -> str:
	data_array = np.array(data)
	array_shape = data_array.shape

	column_widths = []

	for col in range(array_shape[1]):
		max_col_width = 0
		for row in range(array_shape[0]):
			value = data_array[row, col]
			if len(value) > max_col_width:
				max_col_width = len(value)
		column_widths.append(max_col_width)

	csv_string = ''
	horizontal_bar = '+'
	for width in column_widths:
		horizontal_bar += '-' * (width + 2) + "+"

	csv_string += horizontal_bar + '\n'
	for row in range(array_shape[0]):
		csv_string += '| '
		for col in range(array_shape[1]):
			csv_string += f"{data_array[row, col]:<{column_widths[col]}}"
			csv_string += ' | '
		csv_string.rstrip(' ')
		csv_string += "\n"

		if row == 0:
			csv_string += horizontal_bar + '\n'
	csv_string += horizontal_bar

	return csv_string

### testing
def main() -> None:
	csv_data = read_csv("country_data.csv")
	formatted_csv_data = format_list_to_string(csv_data)
	print(formatted_csv_data)

if __name__ == "__main__":
	main()
