
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    is_less_than = False
    if number < cutoff:
        is_less_than = True
        print(f"{number} is less than {cutoff}")
    else:
        print(f"{number} is not less than {cutoff}")

    return is_less_than


def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    if decimal_number == 0:
        return 'Zero'
    try: 
        # Check if decimal_number can be a float
        if isinstance(decimal_number, float):  # This will check if the input is a float
            if decimal_number > 0:
                return 'Positive'
            else:
                return 'Negative'
        else:
            return 'Invalid'  # Not a float
    except:
        return 'Invalid'  # Handle other unexpected errors

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    not_accepted = "invalid"
    if year >= 2001 and year <= 2100:
        year= "21st century"
    elif year >= 1901 and year <=2000:
        year= "20th century"
    elif year >= 1801 and year <=1900:
        year = "19th century"
    elif year < 1801:
        year = "ancient"

    return year

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    
    # Check if all inputs are numbers (int or float)
    if isinstance(number_1, (int, float)) and isinstance(number_2, (int, float)) and isinstance(number_3, (int, float)):
        return max(number_1, number_2, number_3)  
    else:
        return None  


def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    
    # First, check if the scale is valid
    if scale_used not in ['C', 'F']:
        return "Invalid"
    
    # Check if the temperature is a valid number
    if not isinstance(temperature, (int, float)):
        return "Invalid"
    
    if scale_used == 'C':  # Celsius scale
        if temperature <= 0:
            return "Solid"
        elif 0 < temperature < 100:
            return "Liquid"
        else:
            return "Gas"
    
    elif scale_used == 'F':  # Fahrenheit scale
        if temperature <= 32:
            return "Solid"
        elif 32 < temperature < 212:
            return "Liquid"
        else:
            return "Gas"


