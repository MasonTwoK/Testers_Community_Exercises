
def example_1():
    attempt = 0
    correct_password = "1234"

    print("Wellcome ATM app.")

    while attempt < 3:
        user_pin = input("Insert your pin code: ")
        if user_pin == correct_password:
            print("Your balance: 1000 $")
            break
        else:
            print("You entered wrong password")
            attempt += 1

    print("Thank you for using ATM app. Bye!")
