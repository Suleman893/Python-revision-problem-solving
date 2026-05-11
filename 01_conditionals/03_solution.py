username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")
login_attempts = 2
account_blocked = False

# basic validation on username & password:
if username == "" or password == "":
    print("Username or password cannot be empty")
    exit()

# main login check
if username == "admin123":
    
    if password == "pass@123":
        
        if otp == "7788":
            print("Login successful")

            # extra checks after login
            device = input("Is this a trusted device?: ")

            if device == "no":
                print("Additional verification required")

                security_answer = input("What is your favourite color?")

                if security_answer.lower() == "blue":
                    print("Verification successful")
                else:
                    print("Wrong security answer")
            
            # profile completion check
            profile_completed = input("Is profile completed?: ")

            if profile_completed == "no":
                print("Please complete your profile")

            # premium user logic
            premium = input("Premium member?: ")

            if premium == "yes":
                print("Premium features unlocked")
            else:
                print("Using basic account")

        else:
            print("Invalid OTP")
    
    else:
        print("Incorrect password")
        login_attempts -= 1

        if login_attempts == 0:
            account_blocked = True

else:
    print("Username not found")

# final status
if account_blocked:
    print("Account blocked due to multiple failed attempts!!")