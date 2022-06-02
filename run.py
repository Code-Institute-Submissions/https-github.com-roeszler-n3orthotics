"""
Main running file n(3)orthotics order portal
"""
import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')
REGEX_EMAIL = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

user_data = ['f_name', 'l_name', 'user_email']
order_data = ['size_eu', 'height', 'width']
export_data = []


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
    select_option()


def select_option():
    correct = input('Your Selection: ')
    for i in correct:
        if i == '1':
            # print('Updating worksheet and proceeding to order_data...\n')
            # return True
            main()
        elif i == '2':
            print('Taking you to retrieve_order function...\n')
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        else:
            print(f'The number you have provided "{correct}" is not available.\nPlease select again\n')
            select_option()


def instruct_user_data():
    """
    Insruct User on format of first name, last name and email.
    """
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')

    print('First Name: Bobby\nLast Name: Hunden')
    print('Email: bobby123@yourdomain.com\n')
    # get_user_data()


def get_user_data():
    """
    User input of first name, last name and email to from a string
    with fist letter capitalized for names and all lowercase email 
    """
    f_name = remove(input('Your First Name: ').capitalize())
    user_data[0] = f_name
    print(user_data)

    l_name = remove(input('Your Last Name: ').capitalize())
    user_data[1] = l_name
    print(user_data)

    user_email = remove(input('Your Email: ').lower())
    user_data[2] = user_email
    print(user_data)

    validate_user_f_name(f'{f_name}')
    validate_user_l_name(f'{l_name}')
    validate_user_email(f'{user_email}')


def summary_user_data():
    f_name = user_data[0]
    l_name = user_data[1]
    user_email = user_data[2]

    # print(f'\nThanks {f_name}. Your user details are as follows:')
    # print('------------')
    print(f'\nFull Name : {f_name} {l_name}\nEmail : {user_email}')
    # print('------------')


def summary_order_data():
    f_name = user_data[0]
    size_eu = order_data[0]
    height = order_data[1]
    width = order_data[2]

    print(f'\nThanks {f_name}. Your order details are as follows:')
    # print('------------')
    summary_user_data()
    print(f'Shoe Size : EU {size_eu}\nArch Height : {height}\nInsole Width : {width}\n')
    # print('------------')


def validate_user_f_name(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            print('Name is valid...')
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        f_name = remove(input('Your First Name: ').capitalize())
        user_data[0] = f_name
        validate_user_f_name(f_name)
        # print(user_data)

def validate_user_l_name(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            print('Name is valid...')
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        l_name = remove(input('Your Last Name: ').capitalize())
        user_data[1] = l_name
        validate_user_l_name(l_name)
        # print(user_data)


def validate_user_email(user_email):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    values_string = f'{values.split(",")}'
    # print(f'The user_data you provided converted into a list of strings is:\n{values_string}\n')

    try:
        if (re.fullmatch(REGEX_EMAIL, values)):
            print('Email is valid...')
            yes_no_user()
        else:
            raise ValueError(
                f'The email you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Please check the entry and try again.\n')
        user_email = remove(input('Your Email: ').lower())
        user_data[2] = user_email
        print(user_data)
        validate_user_email(values)


def remove(string):
    """
    Removes all spaces in string inputs
    """
    return string.replace(' ', '')


def get_latest_row_entry():
    """
    Prints a list to the termainal of the row last updated
    between colums A to F in the worksheet
    """
    orders = SHEET.worksheet('orders').get_values('A:F')
    latest = orders[-1]
    print(latest)


def yes_no_user():
    """
    Prompt for user to confirm or input correct user_data
    """
    summary_user_data()
    correct = input('\nIs this information correct? y/n: ').lower()
    if correct.startswith('y'):
        f_name = user_data[0]
        print(f'\nThanks {f_name}. Now lets customise your N3 Othoses order...')
        # return True
        get_order_data()
    else:
        get_user_data()


def get_order_data():
    """
    Collection of User input used to order N3D Orthosis.
    """
    get_size_data()
    # get_height_data()
    # get_width_data()


def get_size_data():
    """
    EU shoe size between EU19 and EU50 converted to a float() for order_data
    """
    size_eu = float(input('\nWhat EU Shoe Size would you like to match with?\n(sized in 0.5 increments between 19 and 50): '))
    size_divisble = size_eu % 0.5
    if size_eu >= 19 and size_eu <= 50:
        if size_divisble != 0:
            print(f'\nIncorrect information provided for european shoe sizing: {size_eu}\n')
            get_size_data()
        else:
            order_data[0] = size_eu
            print(order_data)
    else:
        print(f'\nUnfortunatley {size_eu} is not within the european shoe size range we do.\n')
        get_size_data()


def get_height_data():
    """
    Height user input converted into ['Low', 'Med', 'High'] for order_data
    """
    height = remove(input('\nWhat level of support under the inside arch would you like?\n(L: Low Support / M: Medium Support / H: High Support): ').lower())
    if height.startswith('l'):
        order_data[1] = 'Low'
    elif height.startswith('m'):
        order_data[1] = 'Medium'
    elif height.startswith('h'):
        order_data[1] = 'High'
    else:
        print(f'\nIncorrect information provided for arch height: {height}\n')
        get_height_data()
    print(order_data)


def get_width_data():
    """
    Width user input converted into ['Narrow', 'Standard', 'Wide'] for order_data
    """
    width = remove(input('\nWidth of insole to fit the foot &/or shoe\n(N: Narrow / S: Standard / W: Wide): ').lower())
    if width.startswith('n'):
        order_data[2] = 'Narrow'
    elif width.startswith('s'):
        order_data[2] = 'Standard'
    elif width.startswith('w'):
        order_data[2] = 'Wide'
    else:
        print(f'\nIncorrect information provided for insole width: {width}\n')
        get_width_data()
    print(order_data)


def combine_data_for_export():
    for i in user_data:
        order_data.insert(0,i)
    print(order_data)


def clear_screen():
    """
    Checks if Operating System is Mac and Linux or Windows and 
    clears the screen
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    # print("Screen Cleared")


def main():
    """
    Run all program functions
    """
    instruct_user_data()
    # user = get_user_data()


main()

# get_latest_row_entry()
# validate_user_data()
# validate_user_names(values='stuart Roes3ler')
# yes_no_user()
# select_option()
# start()
# get_height_data()
# get_width_data()
# get_size_data()