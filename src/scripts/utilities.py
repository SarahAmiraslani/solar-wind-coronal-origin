from datetime import timedelta, datetime


def convert_fractional_date(number):
    """
    Converts a fractional date to a datetime object.
    
    Parameters:
        number (float): The fractional date to be converted.
        
    Returns:
        datetime: The converted datetime object.
    """
    year = int(number)
    d = timedelta(days=(number - year) * 365)
    day_one = datetime(year, 1, 1)
    date = d + day_one
    return date

