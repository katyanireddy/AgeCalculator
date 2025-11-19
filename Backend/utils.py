"""
Utility functions for Age Calculator
Additional helper functions
"""

from datetime import datetime

def get_zodiac_sign(birth_date):
    """
    Get zodiac sign based on birth date
    
    Args:
        birth_date (datetime): Date of birth
    
    Returns:
        str: Zodiac sign name
    """
    day = birth_date.day
    month = birth_date.month
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius ♒"
    else:
        return "Pisces ♓"

def get_day_of_week(birth_date):
    """
    Get the day of week for birth date
    
    Args:
        birth_date (datetime): Date of birth
    
    Returns:
        str: Day of the week
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[birth_date.weekday()]

def calculate_next_birthday(birth_date):
    """
    Calculate days until next birthday
    
    Args:
        birth_date (datetime): Date of birth
    
    Returns:
        int: Days until next birthday
    """
    today = datetime.now()
    next_birthday = datetime(today.year, birth_date.month, birth_date.day)
    
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
    
    days_until = (next_birthday - today).days
    return days_until
