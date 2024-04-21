# This program simulates a mobile financial application that facilitates bank transactions.

# Print a message to inform users about the purpose of the program.
print("This program simulates a mobile financial application that runs bank transactions")

# Provide users with options to create an account with different banks.
print("""You are allowed to create an account with any of the following banks:
      1. FirstBank
      2. GtBank
      3. UBA""")

# Prompt the user to select a bank to open an account with.
bank = input("Select a bank to open an account with: ")

# Validate the user's input and proceed accordingly.
while True:
    if bank == "1":
        print(f"Welcome to FirstBank of Nigeria. Proceed to create an account with us.")
        break
    elif bank == "2":
        print(f"Welcome to Guarantee Trust Bank. Proceed to create an account with us.")
        break
    elif bank == "3":
        print(f"Welcome to UBA. Proceed to create an account with us.")
        break
    else:
        print("Please select a bank from the provided options.")
        bank = input("Select a bank to open an account with: ")

# Initialize an empty list to store user information.
user = []

# Prompt the user to input their personal information to create an account.
Fname = input("First name: ")
Sname = input("Second name: ")
pword = input("Select a four-digit password: ")
pword1 = input("Confirm your password: ")

# Validate the password to ensure it matches the confirmation.
user.append(Fname)
user.append(Sname)
while True:
    if pword != pword1:
        pword1 = input("Password does not match. Try again: ")
    else:
        break
user.append(pword)

# Prompt the user to input their phone number.
phonum = input("Phone number: ")

# Validate the phone number to ensure it has 11 digits.
while True:
    if len(phonum) != 11:
        print("Phone number must be eleven digits.")
        phonum = input("Phone number: ")
    else:
        user.append(phonum)
        # Confirm successful account creation and provide account details.
        print(f"""Congratulations on opening an account with us. Your new account details are as follows:
              Account Name: {Fname} {Sname} 
              Account Number: {phonum[1:]}""")
        break

# Initialize account balance.
acc = 0

# Prompt the user to log in with their account details.
print("\n\n Login")
phonumb = input("Phone number: ")
paword = input("Password: ")

# Validate the user's login credentials.
while True:
    if (phonumb != phonum and pword != paword) or (phonumb == phonum and pword != paword) or (phonum != phonumb and pword == paword):
        print("Incorrect phone number and password.")
        phonumb = input("Phone number: ")
        paword = input("Password: ")
    else:
        # Display a welcome message upon successful login.
        print("Welcome", Fname + ",", "Enjoy free and seamless banking")
        print("Account Balance = #00")
        
        # Provide options for performing transactions.
        while True:
            tran = input("Would you like to perform a transaction? Yes or No: ")
            if tran == "No":
                break
            elif tran == "Yes":
                oper = input("""Select an operation from the following options:
                    1. Deposit
                    2. Transfer
                    3. Buy Airtime
                    4. Buy Data
                    5. Pay for Utility
                    :   """)
                # Process the selected operation.
                if oper == "1":
                    # Deposit operation
                    x = 3
                    amount = int(input("Amount: # "))
                    sbank = input("Source Bank: ")
                    paword = input("Password: ")
                    while x > 0:
                        if pword != paword:
                            paword = input("Incorrect password. " + str(x - 1) + " trials left: ")
                            x -= 1
                            if x == 0:
                                print("Sorry! Transaction failed.")
                        else:
                            acc += amount
                            print("Transaction successful. Account balance: #", acc, ":00k")
                            break
                    # Prompt for another transaction.
                    tran = input("Would you like to perform another transaction? Yes or No: ")
                    if tran == "Yes":
                        continue
                    else:
                        break
                # Handle other transaction operations similarly.
                # ...
            else:
                print("Response must be Yes or No.")
                tran = input("Would you like to perform a transaction? Yes or No: ")
                break
        break
