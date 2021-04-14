def init():
    isValidOptionSelected = False
    print("Welcome to bankGOODIE")

    while isValidOptionSelected == False:
        have_account = int(input("Do you have an account with us?\n1. Yes\n2. No"))

        if have_account == 1:
            isValidOptionSelected == True
            login()
        elif have_account == 2:
            isValidOptionSelected == True
            register()
        else:
            print("You have selected invalid option")

def login():
    pass

def register():
    pass
