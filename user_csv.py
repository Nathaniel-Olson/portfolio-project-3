# user_csv.py
# ENDG 233 F24
# Nate Olson, Ruald James
# Pairs L01 - 26
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

### imports

def read_csv(filename: str, include_headers: bool = True) -> list[list]:
	"""Reads a file given a file path.
	Parameters:
		filename: name of the file in the 'data_files' folder
		include_headers: whether or not the headers should be included

	Returns:
		csv_data: a 2d list containing the data from the file.
	"""

	# open the file
	csv_file = open(f"data_files/{filename}", 'r')
	csv_data = []

	# for each line in the file
	for index, line in enumerate(csv_file):
		# for the first row only
		if index == 0:
			# if include_headers is true
			if include_headers:

				# split the string into its components, and add them to the data list
				headers = line.strip('\n').split(',')
				csv_data.append(headers)

		# for every other row
		else:
			# split the string into its components
			data_row = line.strip('\n').split(',')

			# check to see if the value is a number
			for index, value in enumerate(data_row):

				# if there is a minus sign
				if value[0] == '-':
					if value[:-1].isdigit():
						data_row[index] = float(value)

				# if it is a numerical digit
				if value.isdigit():
					data_row[index] = float(value)

			# add it to the list
			csv_data.append(data_row)

	# close the file
	csv_file.close()
	return csv_data
	
def write_csv(filename: str, data: list[list], overwrite: bool) -> None:
	"""Write to a file in data_files, creating a new one if it doesn't exist.
	Parameters:
		filename: name of the file in the 'data_files' folder
		data: 2d list of the data to write
		overwrite: T/F indicator of whether to append (False) or over-write (True)
	Returns:
		None
	"""

	# open the file in either write or append mode depending on 'overwrite'
	if overwrite:
		csv_file = open(f"data_files/{filename}", "w") # write mode
	else:
		csv_file = open(f"data_files/{filename}", "a") # append mode

	# for each row in the given data
	for data_row in data:

		# create an empty string to store the data
		data_string = ''

		# add the value, followed by a comma, and at the end of the line, a newline.
		for value in data_row:
			data_string += str(value)
			data_string += ','
		data_string += '\n'
		csv_file.write(data_string)
	return None

# testing
if __name__ == "__main__":
	csv_data = read_csv("country_data.csv")
	modified_data = []
	for i in range(len(csv_data) - 145):
		modified_data.append(csv_data[i])

	write_csv("modified_country_data.csv", modified_data, True)