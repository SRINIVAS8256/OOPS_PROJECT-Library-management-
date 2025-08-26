class Auth:
    def __init__(self):
        self.pin=None
        self.gmail=None
        self.menu()
    def menu(self):
        while(True):
            print("""
            1.signup
            2.Login
            """)
            choice =int(input("Select your choice:"))
            if choice==1:
                self.create_pin()
            if choice == 2:
                self.login()
            else:
                print("select correct choice")


    def create_pin(self):
        self.create_pin=int(input("create your pin"))
        print("pin created successfully")

    def login(self):
        self.verify_pin()
            #home


    def verify_pin(self):
        self.pin=int(input("enter your pin"))
        if self.pin == self.create_pin:
            print("pin is correct,welcome")
        else:
            print("wrong pin")

s=Auth()
