"""
Main program for Age Calculator
Run this file to start the calculator
"""

from age_calculator import calculate_age, validate_date, display_age

def main():
    """Main function to run the age calculator"""
    print("\n" + "="*50)
    print("WELCOME TO AGE CALCULATOR".center(50))
    print("="*50)
    print("\nThis program calculates your exact age.")
    print("Enter your date of birth in DD-MM-YYYY format")
    print("Example: 15-08-2005 or 15/08/2005\n")
    
    while True:
        birth_date_str = input("Enter your date of birth: ").strip()
        
        if birth_date_str.lower() == 'exit':
            print("\nThank you for using Age Calculator! Goodbye!\n")
            break
        
        birth_date = validate_date(birth_date_str)
        
        if birth_date:
            age = calculate_age(birth_date)
            display_age(age)
            
            # Ask if user wants to calculate again
            choice = input("Calculate another age? (yes/no): ").strip().lower()
            if choice not in ['yes', 'y']:
                print("\nThank you for using Age Calculator! Goodbye!\n")
                break
        else:
            print("\nInvalid date format! Please use DD-MM-YYYY format.")
            print("Example: 15-08-2005 or 15/08/2005")
            print("(Type 'exit' to quit)\n")

if __name__ == "__main__":
    main()
