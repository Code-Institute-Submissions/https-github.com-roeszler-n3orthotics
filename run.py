"""
Main running file n(3)orthotics order portal
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')

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

    print(f'\nThanks {f_name}. Your user details are as follows:')
    print('------------')
    print(f'Full Name: {f_name.capitalize()} {l_name.capitalize()}\nEmail: {user_email.lower()}')
    print('------------\n')

def main():
    """
    Run all program functions
    """
    user = get_user_data()
main()
