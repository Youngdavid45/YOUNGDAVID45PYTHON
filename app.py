import random
import string


def user_data():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")

    info_provided = [first_name, last_name, email]

    return info_provided


def password_provided(info_provided):
    letters = string.ascii_letters
    password = f"{info_provided[0][0:2]}{info_provided[1][-2:]}{(''.join(random.choice(letters)for i in range(5)))}"

    return password


employee_new = True

container = []

while employee_new:
    info_provided = user_data()
    password = password_provided(info_provided)
    print(f"Password is {password}")

    is_satisfied = input("Are you ok with generated password:[yes/no] ")

    password_loop = True

    while password_loop:
        if is_satisfied == "yes":
            info_provided.append(password)
            container.append(info_provided)

            password_loop = False

        else:
            d_password = input("Desired password should be longer than 7: ")

            key_len = True

            while key_len:
                if len(d_password) >= 7:
                    info_provided.append(d_password)
                    container.append(info_provided)

                    key_len = False
                    password_loop = False

                else:
                    print("Password is less than 7 characters")
                    d_password = input("Desired password should be longer than 7: ")

        new_employee = input("New employee:[yes/no] ")

        if new_employee == "no":
            employee_new = False
            for item in container:
                print(f"Employee details {item} ")

        else:
            employee_new = True
