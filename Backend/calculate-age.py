"""
Age Calculator
A simple Python program to calculate age from date of birth
"""

from datetime import datetime

def calculate_age(birth_date):
    """
    Calculate age from birth date
    
    Args:
        birth_date (datetime): Date of birth
    
    Returns:
        dict: Dictionary containing years, months, and days
    """
    today = datetime.now()
    
    # Calculate years
    years = today.year - birth_date.year
    
    # Calculate months
    months = today.month - birth_date.month
    
    # Calculate days
    days = today.day - birth_date.day
    
    # Adjust if days are negative
    if days < 0:
        months -= 1
        # Get days in previous month
        if today.month == 1:
            prev_month = 12
            prev_year = today.year - 1
        else:
            prev_month = today.month - 1
            prev_year = today.year
        
        days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days if prev_month < 12 else 31
        days += days_in_prev_month
    
    # Adjust if months are negative
    if months < 0:
        years -= 1
        months += 12
    
    return {
        'years': years,
        'months': months,
        'days': days
    }

def validate_date(date_str):
    """
    Validate and parse date string
    
    Args:
        date_str (str): Date string in format DD-MM-YYYY or DD/MM/YYYY
    
    Returns:
        datetime: Parsed datetime object or None if invalid
    """
    formats = ['%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y']
    
    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            if date_obj > datetime.now():
                print("Error: Birth date cannot be in the future!")
                return None
            return date_obj
        except ValueError:
            continue
    
    return None

def display_age(age_data):
    """
    Display age in a formatted way
    
    Args:
        age_data (dict): Dictionary containing years, months, and days
    """
    print("\n" + "="*50)
    print("YOUR AGE CALCULATION RESULT".center(50))
    print("="*50)
    print(f"Years:  {age_data['years']}")
    print(f"Months: {age_data['months']}")
    print(f"Days:   {age_data['days']}")
    print("="*50)
    print(f"\nYou are {age_data['years']} years, {age_data['months']} months, and {age_data['days']} days old.")
    
    # Calculate total days lived
    total_days = age_data['years'] * 365 + age_data['months'] * 30 + age_data['days']
    print(f"Approximately {total_days:,} days lived!")
    print("="*50 + "\n")
