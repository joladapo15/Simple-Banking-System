#1 password encryption
def encrypt_password(password):
    encrypted = []
    for char in password:
        if "A" <= char <= "Z":
            encrypted.append(chr((ord(char) - ord("A") + 3) % 26 + ord("A")))
        elif "a" <= char <= "z":
            encrypted.append(chr((ord(char) - ord("a") + 3) % 26 + ord("a")))
        elif "0" <= char <= "9":
            encrypted.append(chr((ord(char) - ord("0") + 3) % 10 + ord("0")))
        else:
            encrypted.append(char)
    return "".join(encrypted)


#2 account transactions
class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit_amount(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Updated balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw_amount(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Updated balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")


#3 account information and Authentication
class BankSystem:
    def __init__(self):
        self.users = {}  # Stores user data
        self.logged_in_user = None

    def register_user(self, user_id, password, initial_balance):
        if user_id in self.users:
            print("User ID already exists.")
        else:
            self.users[user_id] = {
                "password": encrypt_password(password),
                "account": BankAccount(initial_balance)
            }
            print("Account created successfully!")

    def login_user(self, user_id, password):
        if user_id in self.users and self.users[user_id]['password'] == encrypt_password(password):
            print(f"User {user_id} logged in successfully.")
            return True
        else:
            print("Invalid user ID or password.")
            return False

    def run(self):
        print("Welcome to the Simple Banking System")

        # Register a new user initially
        user_id = input("Enter new user ID: ").strip()
        password = input("Enter password: ").strip()
        while True:
            try:
                initial_balance = float(input("Your balance: $").strip())
                break
            except ValueError:
                print("Invalid amount. Please enter a number")

        self.register_user(user_id, password, initial_balance)
        self.logged_in_user = user_id  # Log the user in immediately

        while True:
            print("\n*********************** MENU ***********************")
            print("Select a service:")
            print("1. Login to Account")
            print("2. Deposit to Account")
            print("3. Withdraw from Account")
            print("4. Print Balance")
            print("5. Change Password")
            print("6. Exit/Logout")
            print("***************************************************")

            choice = input("Enter choice> ").strip()

            if choice == "1":
                user_id = input("Enter user ID: ").strip()
                password = input("Enter password: ").strip()
                if self.login_user(user_id, password):
                    self.logged_in_user = user_id

            elif choice == "2":
                if self.logged_in_user:
                    try:
                        amount = float(input("Deposit amount: $").strip())
                        self.users[self.logged_in_user]['account'].deposit_amount(amount)
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                else:
                    print("Please log in first.")

            elif choice == "3":
                if self.logged_in_user:
                    try:
                        amount = float(input("Withdrawal amount: $").strip())
                        self.users[self.logged_in_user]['account'].withdraw_amount(amount)
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                else:
                    print("Please log in first.")

            elif choice == "4":
                if self.logged_in_user:
                    balance = self.users[self.logged_in_user]['account'].balance
                    print(f"{self.logged_in_user} balance: ${balance:.2f}")
                else:
                    print("Please log in first.")

            elif choice == "5":
                if self.logged_in_user:
                    new_password = input("Enter new password: ").strip()
                    self.users[self.logged_in_user]['password'] = encrypt_password(new_password)
                    print("Password updated successfully.")
                else:
                    print("Please log in first.")

            elif choice == "6":
                print(f"User {self.logged_in_user} logged out of the account.")
                print("Thank you for using the Simple Banking System!")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the banking system
bank_system = BankSystem()
bank_system.run()