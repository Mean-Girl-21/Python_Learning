"""Created a User class and defined the privileges of the admin."""


class User:
    """Represents a user with a first and last name."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name  

    def describe_user(self):
        print("User Details :")
        print(f"First Name : {self.first_name} , Last Name : {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} !")


class Privileges:
    """Describes the privileges of the administrator (a special kind of user)."""

    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
        ]  # This attribute stores the list of privileges

    def show_privileges(self):
        print(f"\nThe admin has the following priveleges :\n")
        for index, priv in enumerate(self.privileges, start=1):
            print(f"{index}. {priv.title()}")


class Admin(User):
    """Represents an administrator with special user privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.admin_privileges = Privileges()  # Here, python creates a Privileges object (composition) and stores it inside admin_privileges attribute


admin = Admin("Jonathan", "Woodland")
admin.admin_privileges.show_privileges()
