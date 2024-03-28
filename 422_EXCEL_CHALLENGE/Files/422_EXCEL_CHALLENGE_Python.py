# Re-defining the functions to check leap years for both the Gregorian and Revised Julian calendars

def is_leap_gregorian(year):
    # Leap year rule for Gregorian calendar
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_leap_revised_julian(year):
    # Leap year rule for Revised Julian calendar
    return year % 4 == 0 and (year % 100 != 0 or year % 900 == 200 or year % 900 == 600)

# Initialize an empty list to store years where the leap year status disagrees
disagreement_years_list = []

# Iterate over each year in the range
for year in range(1901, 10000):
    # Check leap year status for both calendars
    gregorian = is_leap_gregorian(year)
    revised_julian = is_leap_revised_julian(year)
    
    # If the leap year status disagrees, add the year to the list
    if gregorian != revised_julian:
        disagreement_years_list.append(year)

disagreement_years_list