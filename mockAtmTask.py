# Initializing the system
import random
from datetime import datetime

# datetime object containing current date and time
dateTime = datetime.now()

# prints current date and time
print(dateTime)

database = {}  # dictionary


# Welcome page of our banking app
def init():
    print("Welcome to bankPYTHON")

    have_account = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


# Login function. This allows the user to login to his/her account
def login():
    print("********* Login ***********")

    account_number_from_user = int(input("What is your account number? \n"))
    allowed_password = input("What is your password \n")

    for account_number, user_details in database.items():
        if account_number == account_number_from_user:
            if user_details[3] == allowed_password:
                # datetime object containing current date and time when user logged in
                date_time = datetime.now()
                dt_string = date_time.strftime("%d/%m/%Y at %H:%M:%S")
                # prints current date and time and a welcome message for the user
                print("You logged in on", dt_string)
                bank_operation(user_details)
            else:
                print('Invalid account or password')
                login()
        else:
            print('Invalid account or password')
            login()


# Register function. This allows any user to register an account on the app
def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your account has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


# Operations function. This allows the user to select the operation he/she wants to perform
def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do?\nThese are the available options:\n(1) Cash Deposit"
                                "\n(2) Withdrawal\n(3) Complaint\n(4) Logout\n(5) Exit\n"))

    if selected_option == 1:
        print('You selected %s' % selected_option)
        deposit_operation()
    elif selected_option == 2:
        print('You selected %s' % selected_option)
        withdrawal_operation()
    elif selected_option == 3:
        print('You selected %s' % selected_option)
        complaint_operation()
    elif selected_option == 4:
        print('You selected %s' % selected_option)
        logout()
    elif selected_option == 5:
        print('You selected %s' % selected_option)
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


# Withdrawal function
def withdrawal_operation():
    withdrawal_amount = float(input('How much would you like to withdraw?\n'))
    print("You have withdrawn: $%s" % withdrawal_amount)
    print("Take your cash")
    exit_operation()


# Deposit function
def deposit_operation():
    balance = 0
    deposit_amount = float(input("How much would you like to deposit?\n"))
    balance = balance + deposit_amount
    print('Your balance is: $%s' % balance)
    exit_operation()


# Complaint function
def complaint_operation():
    complaint = input("What issue will you like to report?\n")
    print(f"Your complained about {complaint} and it has been registered.\nThank you for contacting us")
    exit_operation()


# Function to generate account number
def generation_account_number():
    return random.randrange(1111111111, 9999999999)


# Logout function
def logout():
    login()


# Function to ask user if he/she wants to perform another operation or not
def exit_operation():
    exit_response = int(input("Do you want to perform another operation: 1 (yes) 2 (no) \n"))

    if exit_response == 1:
        init()
    else:
        print("Thank you for banking with us")
        exit()


# ACTUAL BANKING SYSTEM


init()

