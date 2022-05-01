from menus.main_menu import Main_menu


class Session:
    def __init__(self):
        self.sendEmail = False
        self.emails = []
        self.secret_in_file = False

    def run(self):
        while True:
            try:
                Main_menu(self).run()
                break
            except Exception as e:
                print(e)
