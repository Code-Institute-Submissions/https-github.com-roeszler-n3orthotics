"""
Main running file n(3)orthotics order portal
"""
import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')
REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# sales = SHEET.worksheet('orders')
# data = sales.get_all_values()
# print(data)


def start():
    """
    Start screen prompting user to:
    1. Create a new order, or
    2. Retrieve an exsisting order with order number
    """
    print('Welcome to N(3)ORTHOTICS order portal.\n')
    print('Use this app to directly access made-to-order N3D Printed Insoles')
    print('Please visit northotics.com/home for more information\n')
    print('Select 1. : Place a new N3D insole order')
    print('Select 2. : Retrieve an exsisting N3D order')
    print('Select 3. : Exit Program\n')
    # select_option()


def get_user_data():
    """
    Get User first name, last name and email from user as a string
    """
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    print('First Name: Bobby\nLast Name: Hunden')
    print('Email: bobby123@yourdomain.com\n')

    f_name = input('Your First Name: ')
    l_name = input('Your Last Name: ')
    user_email = input('Your Email: ')

    print(f'\nThanks {remove(f_name.capitalize())}. Your user details are as follows:')
    print('------------')
    print(f'Full Name: {remove(f_name.capitalize())} {remove(l_name.capitalize())}\nEmail: {remove(user_email.lower())}')
    print('------------\n')
    yes_no_user()
    validate_user_data(f'{remove(f_name.capitalize())}, {l_name.capitalize()}, {user_email.lower()}')

def remove(string):
    return string.replace(' ', '')

def validate_user_data(values):
    """
    Inside the try, converts all user_email inputs into floats.
    Raises ValueError if strings cannot be converted into float or
    if height == low or mid or high string values or 
    if width == narrow or standard or wide.
    """
    print(f'The data you provided converted into a list of strings is:\n{remove(values)}\n')



def yes_no_user():
    correct = input('Is this information correct? y/n: ').lower()
    if correct.startswith('y'):
        # print(f'Thanks *** , updating worksheet and proceeding to order_data\n')
        return True
    else:
        get_user_data()


def main():
    """
    Run all program functions
    """
    user = get_user_data()
main()
