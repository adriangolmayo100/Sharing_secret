from input import input_application


class Settings_menu:
    def __init__(self, session):
        self.session = session

    def run(self):
        finish = False
        option = 0

        while not finish:
            print("\nSETTINGS MENU")
            print("1. Set whether you want an e-mail with the keys to be sent or the keys displayed on the screen.")
            print("2. Set whether you want to write your secret or read it from a file.")
            print("3. Exit.")
            print("Choose an option.")

            option = input_application.request_integer()

            if option == 1:
                self.change_send_mail()
            elif option == 2:
                self.change_secret_in_file()
            elif option == 3:
                finish = True
            else:
                print("Write a number between 1 and 2.")

    def change_send_mail(self):
        finish = False
        option = 0
        print("\nINPUT OPTION")
        print("Set whether you want to send e-mails to the people with the keys or if they show up in the prompt.")
        while not finish:

            print("1. Send e-mail with keys.")
            print("2. Write in the terminal the keys.")

            option = input_application.request_integer()

            if option == 1:
                self.session.sendEmail = True
                finish = True
            elif option == 2:
                self.session.sendEmail = False
                finish = True
            else:
                print("Write 1 or 2.")

    def change_secret_in_file(self):
        finish = False
        option = 0
        print("\nINPUT OPTION")
        print("Set whether you want to write your sharing secret or read it from a file.")
        while not finish:

            print("1. Read from file the secret.")
            print("2. Write in the terminal the secret.")

            option = input_application.request_integer()

            if option == 1:
                self.session.secret_in_file = True
                finish = True
            elif option == 2:
                self.session.secret_in_file = False
                finish = True
            else:
                print("Write 1 or 2.")
