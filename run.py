"""
Main running file n(3)orthotics order portal
"""
import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email
import os
import datetime
from datetime import timezone

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
order_data = [
    'size_eu', 'height', 'width', 'order_no', '', 'order_status', '', 'row_no'
    ]
update_order = ['order_status', 'order_update']
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
    # select_option()


def select_option():
    """
    Initial user choice to place a new or retieve an exsisting N3D order
    """
    correct = input('Your Selection: ')
    for i in correct:
        if i == '1':
            # print('Updating worksheet and proceeding to order_data...\n')
            # order_data.clear()
            # export_data.clear()
            return True
            # main()
        elif i == '2':
            clear_screen()
            print('Retieve an esxisting N3D insole order : \n')
            display_order()
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        elif i == '3':
            clear_screen()
            quit()
        else:
            print(
                f'The number you have provided "{correct}" is not available.')
            print('Please select again\n')
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
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [0] of the 
    user_data list = f_name
    """
    # f_name = (f'{values}')
    # print(values)
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            # print('Name is valid...')
            # f_name = values
            user_data[0] = values.capitalize()
            # print(values)
            # return True
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        f_name = remove(input('First Name details: ').capitalize())
        user_data[0] = f_name
        # print(user_data[0])
        validate_user_f_name(f_name)
        # print(user_data)
    # else:
    #     f_name = (f'{values}')
    #     user_data[0] = f_name


def validate_user_l_name(values):
    """
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [1] of the 
    user_data list = l_name
    """
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            user_data[1] = values.capitalize()
            print(user_data[1])
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        l_name = remove(input('Last Name details : ').capitalize())
        user_data[1] = l_name
        print(user_data[1])
        validate_user_l_name(l_name)
        # print(user_data)


def validate_user_email(values):
    """
    Inside the try, checks all user email input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [2] of the 
    user_data list = user_email
    """
    values_string = f'{values.split(",")}'
    # print(f'The user_data you provided converted into a list of strings is:\n{values_string}\n')
    try:
        if (re.fullmatch(REGEX_EMAIL, values)):
            # print('Email is valid...')
            user_data[2] = values.lower()
            # yes_no_user()
        else:
            raise ValueError(
                f'The email you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as error:
        print(f'\nInvalid data: {error}. Please check the entry and try again.\n')
        user_email = remove(input('Your Email: ').lower())
        user_data[2] = user_email
        validate_user_email(user_email)
        # print(user_data)


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


ef yes_no_user():
    """
    Prompt for user to confirm or input correct user_data
    """
    summary_user_data()
    correct = input('\nIs this information correct? y/n: ').lower()
    if correct.startswith('y'):
        f_name = user_data[0]
        print(f'\nThanks {f_name}. Now lets customise your N3 Othoses order...')
        get_order_data()
        generate_order_no()
        combine_data_for_export()
        summary_order_data()
        submit_order()
        # return True
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
    Converts to a float() between EU shoe size between EU19 and EU50 only.
    Inside the try, converts all string values into floating points and
    raises ValueError if not a number.
    """
    while True:
        try:
            size_eu = float(remove(input('\nWhat EU Shoe Size would you like to fit into?\n(sized in 0.5 increments between 19 and 50): ')))
            size_divisble = size_eu % 0.5

            if size_eu >= 19 and size_eu <= 50:
                if size_divisble != 0:
                    print(f'\nIncorrect information provided for european shoe sizing: {size_eu}\n')
                    get_size_data()
                else:          
                    order_data[0] = size_eu
                    return size_eu
            else:
                print(f'\nUnfortunatley {size_eu} is not within the european shoe size range we do.\n')
                get_size_data()

        except ValueError as e:
            print(f'Invalid data : {e}, please try again.\n')
            # return False
            continue
        return True


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
        # generate_order_no()
        # submit_order()
    elif width.startswith('s'):
        order_data[2] = 'Standard'
        # generate_order_no()
        # submit_order()
    elif width.startswith('w'):
        order_data[2] = 'Wide'
        # generate_order_no()
        # submit_order()
    else:
        print(f'\nIncorrect information provided for insole width: {width}\n')
        get_width_data()


def combine_data_for_export():
    for i in user_data:
        export_data.append(i)
    for i in order_data:
        export_data.append(i)
    # print(order_data)


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


def slice_last_order_no():
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = last_entry[0]
    x = slice(6)
    reset_no = int(last_entry_int[x])
    reset_no_10K = reset_no * 10000
    # print(type(reset_no))
    return reset_no_10K


def generate_order_no():
    """
    
    """
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = int(last_entry[0])
    now = datetime.datetime.now()
    order_date = now.strftime('%y%m%d')
    new_order_no = (int(order_date)*10000) + (last_entry_int - slice_last_order_no() + 1)

    order_data[3] = new_order_no
    # print(type(new_order_no))
    # print(new_order_no)
    # print(type(order_data[3]))
    # print(order_data[3])
    return new_order_no


# def generate_date_time():
#     now = datetime.datetime.now()
#     order_date = now.strftime('%y%m%d')
#     n = int(order_date)
#     # order_date[0] = order_date
#     print(f"Order Prefix: {n}")
#     print(type(n))
#     print(n)
#     order_date = n


def generate_UTC_time():
    """
    Creates Central European Standard Time (CEST) version of date and time
    in iso 
    """
    utc_now = datetime.datetime.now(timezone.utc)
    # CEST = pytz.timezone('Europe/Stockholm')
    # UTC = pytz.timezone('Etc/GMT+0')
    # print('{} CEST'.format(utc_now.astimezone(CEST).isoformat()))
    # print('{} UTC'.format(utc_now.astimezone().isoformat()))
    # print('the supported timezones by the pytz module:', pytz.all_timezones, '\n')
    # n = '{}'.format(utc_now.astimezone(CEST).isoformat())
    n = '{}'.format(utc_now.astimezone(UTC).isoformat())
    # print(export_data)
    return n


def update_date_ordered():
    """
    Updates the order_date filed within order_data list
    """
    n = generate_UTC_time()
    order_data[4] = n
    order_data[5] = 'NEW ORDER'
    print(order_data)


def input_order_no():
    """
    Checks the user input order number is only numerical and correct length
    """
    print('Please enter your order number below.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    print('Example Number: 2205190003\n')
    while True:
        try:
            order_no = int(remove(input('Order Number: ')))
            order_no_string = str(order_no)
            if len(order_no_string) != 10:
                raise ValueError(
                f'`Our order numbers require 10 digits.\nUnfortunatley {order_no} has {len(order_no_string)} digits.'
                )
        except ValueError as e:
            print(f'Invalid data : {e}\nPlease check your records and try again below;\n')
            # return False
            continue
        print(len(order_no_string))
        print(order_no)
        # return True
        return order_no


def retrieve_order():
    """
    Searches worksheet coloum order_no for a match to user input and
    returns row information to local user_data, oder_data and export_data lists
    """
    search_input = str(input_order_no())
    order_nos_import = SHEET.worksheet('orders').get_values('G:G')
    order_nos = flatten_nested_list(order_nos_import)
   
    res = [i for i in range(len(order_nos)) if order_nos[i] == search_input]
    if res == []:
        print(f'Order number {search_input} not found?!\n')
        retrieve_order()
    else:
        for i in range(len(order_nos)):
            if search_input == order_nos[i]:
                search_res_row = i+1
                print(f'\nOrder found in database row no.{search_res_row}')
                # search_res_row = order_data[7]
                return search_res_row


def display_order():
    """
    
    """
    row = int(retrieve_order())
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    flat_order = flatten_nested_list(order_row)
    
    # converts back to an integer
    size_eu = flat_order[3]
    flat_order[3] = int(size_eu) 
    order_no = flat_order[6]
    flat_order[6] = int(order_no)
    user_data[0:3] = flat_order[0:3]
    order_data[0:6] = flat_order[3:9]
    order_data[7] = int(row)
    combine_data_for_export()
  
    print('\nYour order details are as follows:\n')
    print(f'Full Name : {user_data[0]} {flat_order[1]}\nEmail : {flat_order[2]}')
    print(f'Shoe Size : EU {flat_order[3]}\nArch Height : {flat_order[4]}\nInsole Width : {flat_order[5]}')
    print(f'Order No. : {flat_order[6]}\nDate Ordered : {flat_order[7]}\nCurrent Status : {flat_order[8]}')
    print(f'Place in production queue : {flat_order[10]}\n')
    update_status()


def change_feat():
    """
    
    """
    i = input('Your Selection : ')
    if i == '1':
        clear_screen()
        f_name = input('New First Name details: ')
        validate_user_f_name(f_name)
        f_name = user_data[0]
        # print(f_name)
        # export_data[0] = f_name
        validate_change_feat()
    #     print(f'user_data:\n {user_data}')
    #     print(order_data)
    #     print(f'order_data:\n {order_data}')
    #     print(export_data)
    #     print(f'export_data:\n {export_data}')
    #     print(flat_order)
    #     print(f'flat_order:\n {flat_order}')
    elif i == '2':
        clear_screen()
        l_name = input('New Last Name details: ')
        validate_user_l_name(l_name)
        l_name = user_data[1]
        # print(user_data[1])
        validate_change_feat()
    elif i == '3':
        clear_screen()
        user_email = input('New Email details: ')
        validate_user_email(user_email)
        user_email = user_data[2]
        # print(user_data[2])
        validate_change_feat()
    elif i == '4':
        print('size_eu : ')
    elif i == '5':
        print('Height : ')
    elif i == '6':
        print('Width : ')
    elif i == '7':
        print('Submit : ')
        combine_data_for_export()
        print(export_data)
    elif i == '8':
        main()
    else:
        print(f'The number you have provided "{selection}" is not part of this selection.\nPlease select again\n')
        validate_change_feat()


def validate_change_feat():
    """
    Valudates order is prior to 'SUBMITTED TO PRINT' stage for change_feat function
    """
    row = order_data[7]
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    flat_order = flatten_nested_list(order_row)

    print(f'Current order status is: {flat_order[8]}')
    if flat_order[8] == 'PENDING' or flat_order[8] == 'NEW ORDER' or flat_order[8] == 'CREATED' or flat_order[8] == 'ACCEPTED' or flat_order[8] == 'DESIGNED':
        print('Order is modifiable.')
        print('\nYour order details are as follows:\n')
        print(f'Order No. : {flat_order[6]}\nDate Ordered : {flat_order[7]}\nPlace in production queue : {flat_order[10]}\nCurrent Status : {flat_order[8]}')
        print('\nDetails you can edit:\n')
        print(f'1. First Name : {user_data[0]}\n2. Surname : {user_data[1]}\n3. Email : {user_data[2]}')
        print(f'4. Shoe Size : EU {order_data[0]}\n5. Arch Height : {order_data[1]}\n6. Insole Width : {order_data[2]}\n')
        print(f'7. Submit the above details\n8. Take me Home\n')
        change_feat()

    else:
        print(f'Unfortunately, at the {flat_order[8]} stage, this order is past the point\nwhere modifications can occur without charges.')
        email_print_update_startover()


def update_status():
    """
    
    """
    order_no = order_data[3]
    f_name = user_data[0]
    # print(export_data)
    print(f'Hi {f_name}. What would you like to do with order no.{order_no} ?')
    print('\nSelect 1. : Re-Print this order again (no changes)')
    print('Select 2. : Change the features')
    print('Select 3. : Start a new order')
    print('Select 4. : Cancel order')
    print('Select 5. : Search different order')
    print('Select 6. : Take me home\n')
    startover = input('Your Selection: ')
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Re-printing order number : {order_no}...\n')
            submit_order()
            # test_email()
            # email_print_update_startover()
        elif i == '2':
            clear_screen()
            print(f'Order No.{order_no}\n')
            validate_change_feat()
            # email_print_update_startover()
        elif i == '3':
            clear_screen()
            print('Starting a new N3D insole order...')
            yes_no_user()
            # get_order_data()
        elif i == '4':
            clear_screen()
            print(f'Checking the current status of order no.{order_no}...')
            update_to_canceled_status()
        elif i == '5':
            clear_screen()
            display_order()
            # order_no = input(f'Your order no. : {order_no}')
        elif i == '6':
            clear_screen()
            main()
        else:
            print(f'The number you have provided "{startover}" is not available.\nPlease select again\n')
            email_print_update_startover()
    n = generate_UTC_time()
    update_order[1] = n
    print(update_order)
    print(export_data)
    n = generate_UTC_time()
    update_order[1] = n
    print(update_order)
    print(export_data)


def cancel_confirm():
    """
    
    """
    confirm = input('Are you sure you wish to cancel this order? y/n : ')
    if confirm.startswith('y'):
        return True
    elif confirm.startswith('n'):
        main()


def update_to_canceled_status():
    """
    Updates status to pending when user saves order
    """
    row = order_data[7]
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    order_worksheet = SHEET.worksheet('orders') # accessing our order_worksheet from our google sheet

    print(f'\nCurrent order status is: {export_data[8]}\n')

    if export_data[8] == 'PENDING' or export_data[8] == 'NEW ORDER' or flat_order[8] == 'UPDATED ORDER' or export_data[8] == 'CREATED' or export_data[8] == 'ACCEPTED' or export_data[8] == 'DESIGNED':
        # print('true')
        cancel_confirm()
        n = generate_UTC_time()
        export_data[9] = n
        export_data[8] = 'CANCELED'
        order_worksheet.update(f'I{row}', f'{export_data[8]}') # updating cell i in colom I
        order_worksheet.update(f'J{row}', f'{export_data[9]}') # updating cell i in colom J
        print(f'\nOrder successfully CANCELED.')
        print(f"An email with it's credit note details will be sent to {export_data[2]}")
        print(f'\nPlease carefully record the order no.{export_data[6]}\nYou will need it to refer to this action into the future.')
        email_print_update_startover()
    else:
        # print('false')
        print(f'\nUnfortunatley as a custom-to-order product, this order is currently at a point in\nmanufacture that is beyond the point of no return and cannot be canceled or refunded.\n\nFor further clarificaiton of made-to-order products purchased online, please feel free to contact info@northotics.com refering order number {export_data[6]}.\nYour purchasing rights have not been affected.\n')
        email_print_update_startover()


def submit_row_data():
    """
    Replaces the exsisting row data in the worksheet with updated data and 
    records the date of the order update
    """
    row = order_data[7]
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    order_worksheet = SHEET.worksheet('orders')

    print(f'Accessing your order on row number : {row}')
    # print(f'order_row :\n{order_row}')
    # print(f'export_data :\n{export_data}')
    # print(f'order_data :\n{order_data}')
    # print(f'user_data :\n{user_data}')

    n = generate_UTC_time()
    export_data[9] = n
    export_data[8] = 'UPDATED ORDER'
    order_worksheet.update(f'A{row}', export_data[0])
    order_worksheet.update(f'B{row}', export_data[1])
    order_worksheet.update(f'C{row}', export_data[2])
    order_worksheet.update(f'D{row}', int(export_data[3]))
    order_worksheet.update(f'E{row}', export_data[4])
    order_worksheet.update(f'F{row}', export_data[5])
    order_worksheet.update(f'G{row}', int(export_data[6]))
    order_worksheet.update(f'H{row}', export_data[7])
    order_worksheet.update(f'I{row}', export_data[8])
    order_worksheet.update(f'J{row}', export_data[9])

    print(f'\nOrder No.{export_data[6]} successfully updated!\nThanks for using the N(3)Orthotics order submission app.\n\nYou should shortly recieve an email to {export_data[2]} confirming the changes')
    update_status()


def submit_order():
    """
    
    """
    submit = input('Would you like to submit this order? y/n: ').lower()
    if submit.startswith('n'):
        save_order()
    else:
        clear_screen()
        generate_order_no()
        combine_data_for_export()

        update_sales_worksheet(export_data)

        user_email = export_data[2]
        recent_order_no = export_data[6]
        print(f'\nOrder Successfully Submitted!!\nYou will shortly receive an email instructions to:\n {user_email} with the details to arrange secure payment')
        print(f'\nYour order number is: {recent_order_no}')
        summary_order_data()
        email_print_update_startover()


def update_sales_worksheet(data):
    """
    Update sales google worksheet, add new row with the list data provided
    """
    print('Contacting the mothership...')
    order_worksheet = SHEET.worksheet('orders') # accessing our sales_worksheet from our google sheet
    order_worksheet.append_row(data) # adds a new row in the google worksheet selected
    print('Success!! The Northo-bots have made contact!')


def save_order():
    """
    
    """
    save = input('\nWould you like to save this order? y/n: ').lower()
    if save.startswith('n'):
        # user_data.clear()
        order_data.clear()
        export_data.clear()
        clear_screen()
        main()
    else:
        combine_data_for_export()
        summary_order_data()
        email_print_update_startover()


def email_print_update_startover():
    print('\nWhat would you like to do next?')
    print('\nSelect 1. : Email this order')
    print('Select 2. : Print this order')
    print('Select 3. : Start a new N3D insole order')
    print('Select 4. : Retrieve an exsisting N3D order')
    print('Select 5. : Exit this n3orthotics session\n')

    startover = input('Your Selection: ')
    order_no = order_data[3]
    user_email = user_data[2]
    for i in startover:
        if i == '1':
            print(f'Emailing order number : {order_no} to {user_email}...\n')
            email_print_update_startover()
            # main()
        elif i == '2':
            print(f'Printing order number : {order_no}...\n')
            email_print_update_startover()
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        elif i == '3':
            print('Start a new N3D insole order...')
            yes_no_user()
            # get_order_data()
        elif i == '4':
            print('Taking you to retrieve_order function...\n')
        elif i == '5':
            print('Exiting this n3orthotics session...\n')
            clear_screen()
            start()
            select_option()
        else:
            print(f'The number you have provided "{startover}" is not available.\nPlease select again\n')
            email_print_update_startover()


def main():
    """
    Run all program functions
    """
    clear_screen()
    start()
    select_option()
    instruct_user_data()
    get_user_data()
    summary_order_data()
    combine_data_for_export()
    submit_order()

# main()


# get_latest_row_entry()
# validate_user_email(values='stuart@roeszler.com')
# validate_user_names(values='stuart Roes3ler')
# yes_no_user()
# start()
# select_option()
# summary_user_data()
# yes_no_user()
# get_order_data()
# get_size_data()
# summary_order_data()
# submit_order()
# save_order()
# combine_data_for_export()
# clear_screen()
# generate_order_no()
# generate_date_time()
# generate_UTC_time()
# update_date_ordered()
# instruct_user_data()
# email_print_update_startover()
# slice_last_order_no()
# test_email()
# export_to_printer()
# update_status()
# retrieve_order() 
display_order()
# input_order_no()
# update_to_pending_status()
# update_to_canceled_status()
# cancel_confirm()
# validate_change_feat()
