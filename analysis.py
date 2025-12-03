# analysis.py
# ENDG 233 F25
# Nate Olson, Ruald James
# Pairs L01 - 26
# A set of functions for analyzing input data

### imports
import numpy as np
from user_csv import read_csv, write_csv

### functions
def compare_population_densities(country1: str, country2: str) -> np.array:
    """Compares two input countries population densities per year.
    Parameters:
        country1: the first country to analyze
        country2: the second country to analyze
    Returns:
        np.array: a table containing the population densities per year for each country.
    """
    # get the population density array for each country
    country1_pop_densities = population_density_per_year(country1)
    country2_pop_densities = population_density_per_year(country2)
    
    # keep the header row and add the data for each country underneath it
    total_pop_densities = np.vstack((country1_pop_densities, country2_pop_densities[1]))

    # return the array
    return total_pop_densities
	
def compare_endangered_species(country1: str, country2: str) -> np.array:
    """Compares two input countries endangered species per capita.
    Parameters:
        country1: the first country to analyze
        country2: the second country to analyze
    Returns:
        np.array: a table containing the endangered species per capita for each country.
    """
    # get the endangered species per capita array for each country
    country1_endangered_species = endangered_species_per_capita(country1)
    country2_endangered_species = endangered_species_per_capita(country2)

    # keep the header row and add the data for each country underneath it
    total_endangered_species = np.vstack((country1_endangered_species, country2_endangered_species[1]))

    return total_endangered_species

def population_density_per_year(country: str) -> np.array:
    '''Calculates the population density per year for a specified country.
    Parameters:
        country: The name of the country to analyze
    Returns:
        np.array: A 2D array containing the header row and the population densities per year for the specified country
    '''

    # read both the country data and population data as np.arrays
    country_data = np.array(read_csv("country_data.csv", True))
    population_data = np.array(read_csv("population_data.csv", True))

    # iterating over the country data, if the first element (Country) is the same as the input country, then save the index
    for index, row in enumerate(country_data):
        if row[0] == country:
            country_index = index

    # grab the Sq Km from country data and the list of populations from population data, casting both as floats
    size = country_data[country_index][3].astype(float)
    populations = population_data[country_index, 1:].astype(float)

    # create the list of densities per year by dividing population by size
    densities = []
    for pop in populations:
        densities.append(round(pop / size, 2))

    # create the header row, starting with "Country"
    header_row = ["Country"]
	
    # add each subsequent header from the original row plus " Density (pop/km^2)"
    for header in population_data[0]:
        if header != population_data[0][0]:
            header_row += [header + " Density (pop/km^2)"]

    # build the data row, with the country name and the densities from each year
    data_row = [country] + densities

    # build the data table by making a 2d list and turning it into a np.array
    data_table = np.array([header_row, data_row])

    return data_table

def endangered_species_per_capita(country: str) -> np.array:
    """Returns a numpy array of the number of endangered species per capita of a given country.
    Parameters:
        country: The name of the country to analyze
    Returns:
        np.array: A 2D array containing the header row and the number endangered species per capita between years 2000 and 2020 for the specified country
    """

    # read both the population data and endangered species data as np.arrays
    species_data = np.array(read_csv("threatened_species.csv", True))
    
    # iterating over the species data, if the first element (Country) is the same as the input country, then save the index
    print(country)
    for index, row in enumerate(species_data):
        if row[0] == country:
            country_index = index

    # get the mean population and the number of species, casting as a float if need be
    mean_pop = mean_population(country)
    species_counts = species_data[country_index, 1:].astype(float)

    # create the list of densities per year by dividing number of species by average population
    species_per_capita = []
    for count in species_counts:
        species_per_capita.append(f"{count / mean_pop:.2e}")
    
    # create the header row, starting with "Country"
    header_row = ["Country"]

    # add each subsequent header from the original row plus " per Capita"
    for header in species_data[0]:
        if header != species_data[0][0]:
            header_row += [header + " per Capita"]
    
    # build the data row, with the country name and the species per capita
    data_row = [country] + species_per_capita

    # build the data table by making it a 2d list and turning it into a np.array
    data_table = np.array([header_row, data_row])

    return data_table

def maximum_population(country: str) -> float:
    """Returns a float of the maximum population of a given country.
    Parameters:
        country: The name of the country to analyze
    Returns:
        float: The largest population from year 2000 - 2020, inclusive
    """

    # read the population data as an np.array
    population_data = np.array(read_csv("population_data.csv", False))
	
    # iterating over the population data, if the first element (Country) is the same as the input country, then save the index
    for row in population_data:
        if row[0] == country:
            data_row = row
	
    # excluding the first element from the row and casting everything as floats, take the max of the row.
    max_pop = data_row[1:].astype(float).max()
    return max_pop

def mean_population(country: str) -> float:
    """Returns a float of the mean population of a given country from year 2000 - 2020, inclusive.
    Parameters:
        country: The name of the country to analyze
    Returns:
        float: The mean population from year 2000 - 2020, inclusive
    """

    # read the population data as an np.array
    population_data = np.array(read_csv("population_data.csv", False))
	
    # iterating over the population data, if the first element (Country) is the same as the input country, then save the index
    for row in population_data:
        if row[0] == country:
            data_row = row
	
    # excluding the first element from the row and casting everything as floats, take the mean of the row.
    mean_pop = data_row[1:].astype(float).mean()
    return mean_pop

def format_array_to_string(data: np.array) -> str:
    """Formats a given 2d list or np.array into a stylized table for printing.
    Parameters:
        data: 2d list or np.array of information
    Returns:
        str: formatted table of the data
    """

    # get the shape of the array
    array_shape = data.shape

    # create a list to track the width of each column
    column_widths = []

    # iterating over the columns, first set the max width to zero. then, for each row, if its width is larger than the current largest width,
    # set it as the new maximum. finally, append it to the column widths list.
    for col in range(array_shape[1]):
        max_col_width = 0
        for row in range(array_shape[0]):
            value = data[row, col]
            if len(value) > max_col_width:
                max_col_width = len(value)
        column_widths.append(max_col_width)

    # declare the string to hold the finished table
    csv_string = 'Table:\n'

    # build the horizontal bar, with '+' in each corner, and a number of dashes corresponding to the column length
    horizontal_bar = '+'
    for width in column_widths:
        horizontal_bar += '-' * (width + 2) + "+"

    csv_string += horizontal_bar + '\n'

    # put the values at each [row,col] index pair with enough padding to get them to match the column width.
    for row in range(array_shape[0]):
        csv_string += '| '
        for col in range(array_shape[1]):
            csv_string += f"{data[row, col]:<{column_widths[col]}}"
            csv_string += ' | '
        csv_string.rstrip(' ')
        csv_string += "\n"

        # for the header row only, add an extra horizontal bar to distinguish it
        if row == 0:
            csv_string += horizontal_bar + '\n'
    csv_string += horizontal_bar + '\n'

    # return the string
    return csv_string