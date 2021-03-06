def is_leap_year(year):
    if year % 4 != 0:
        return False

    return year % 100 == 0 and year % 400 == 0 or \
        year % 100 != 0 and year % 400 != 0
