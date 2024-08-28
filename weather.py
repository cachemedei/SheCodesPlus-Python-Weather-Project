import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """

    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date_value = datetime.fromisoformat(iso_string)
    formatted_date = date_value.strftime("%A %d %B %Y")
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    
    temp_in_celcius = ((float(temp_in_fahrenheit) - 32) * 5) / 9
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    float_values = list(map(float, weather_data))
    mean_value = sum(float_values) / len(weather_data)

    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    big_list = []

    with open(csv_file) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            if row:
                small_list = [row[0], int(row[1]), int(row[2])]
                big_list.append(small_list)

    return big_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    float_list = [float(value) for value in weather_data]
    min_value = min(float_list)
    min_index = len(float_list) - 1 - float_list[::-1].index(min_value)

    return min_value, min_index
    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    float_list = [float(value) for value in weather_data]
    max_value = max(float_list)
    max_index = len(float_list) - 1 - float_list[::-1].index(max_value)

    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    formatted_data = []

    for item in weather_data:
        day = convert_date(item[0])
        min = convert_f_to_c(item[1])
        max = convert_f_to_c(item[2])
        formatted_data.append([day, min, max])
    
    min_temp_list = []
    max_temp_list = []
    highest_temp = float('-inf')
    lowest_temp = float('inf')
    day_of_highest_temp = ""
    day_of_lowest_temp = ""

    for entry in formatted_data:
        day = entry[0]
        min_temp = entry[1]
        max_temp = entry[2]
        min_temp_list.append(entry[1])
        max_temp_list.append(entry[2])
        
        if max_temp > highest_temp:
            highest_temp = max_temp
            day_of_highest_temp = day
        if min_temp < lowest_temp:
            lowest_temp = min_temp
            day_of_lowest_temp = day

    mean_max_temp = round(sum(max_temp_list) / len(max_temp_list), 1)       
    mean_min_temp = round(sum(min_temp_list) / len(min_temp_list), 1)

    summary_string = (f"{len(weather_data)} Day Overview\n"
    f"  The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {day_of_lowest_temp}.\n"
    f"  The highest temperature will be {format_temperature(highest_temp)}, and will occur on {day_of_highest_temp}.\n"
    f"  The average low this week is {format_temperature(mean_min_temp)}.\n"
    f"  The average high this week is {format_temperature(mean_max_temp)}.\n")
    
    return summary_string


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary = []

    for entry in weather_data:
            day = convert_date(entry[0])
            min = convert_f_to_c(entry[1])
            max = convert_f_to_c(entry[2])

            daily_summary = (
                f"---- {day} ----\n"
                f"  Minimum Temperature: {format_temperature(min)}\n"
                f"  Maximum Temperature: {format_temperature(max)}\n\n"
            )

            summary.append(daily_summary)

    return ''.join(summary)