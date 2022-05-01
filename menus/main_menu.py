import utils
from input import input_application
from menus.settings_menu import Settings_menu
from options import generate_secret, reveal_secret, help


class Main_menu:
    def __init__(self, session):
        self.session = session
        self.settings_menu = Settings_menu(self.session)

    def run(self):
        finish = False
        option = 0
        while not finish:
            print("\nMAIN MENU")
            print("1. Create a sharing secret.")
            print("2. Recover a sharing secret.")
            print("3. Settings.")
            print("4. Help.")
            print("5. Exit.")

            print("Choose an option.")

            option = input_application.request_integer()

            if option == 1:
                self.generate_secret()
            elif option == 2:
                self.reveal_secret()
            elif option == 3:
                self.settings_menu.run()
            elif option == 4:
                help.show()
            elif option == 5:
                finish = True
            else:
                print("Write a number between 1 and 4.")
        print("\n¡Goodbye!")

    def generate_secret(self):
        secret, amount_people, minimum_people = generate_secret.request_data(self.session.secret_in_file)
        keys = generate_secret.run(secret, amount_people, minimum_people)
        self.session.emails = input_application.request_emails(self.session.sendEmail, len(keys))
        utils.show_keys(keys, self.session.sendEmail, self.session.emails)

    def reveal_secret(self):
        amount_people, keys = reveal_secret.request_data()
        secret = reveal_secret.run(keys)
        print(f"The secret code is: {secret}.")
