from dataclasses import dataclass


@dataclass
class Person:
    """
    Class to represent a generic person
    """
    first_name: str = ""
    last_name: str = ""
    email: str = ""

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@dataclass
class Customer(Person):
    """
    Subclass of the Person class
    that adds attribute for customer
    number.
    """
    customer_number: str = ""


@dataclass
class Employee(Person):
    """
    Subclass of the Person class that
    adds attribute for employee SSN
    """
    SSN: str = ""


def main():
    print("Customer/Employee Data Entry\n")
    cont = "y"
    user = None
    while cont.lower() == "y":
        user_type = str(input("customer or employee (c/e): ")).lower()
        if user_type == "c":
            user = Customer()
        elif user_type == "e":
            user = Employee()
        print("\nDATA ENTRY")
        user.first_name = str(input(f"{'First Name:':<12}"))
        user.last_name = str(input(f"{'Last Name:':<12}"))
        user.email = str(input(f"{'Email:':<12}"))

        if isinstance(user, Customer):
            user.customer_number = str(input(f"{'Number:':<12}"))
        elif isinstance(user, Employee):
            user.SSN = str(input(f"{'SSN:':<12}"))
        if isinstance(user, Customer):
            print("\nCUSTOMER")
            print(f"{'Name:':<12}{user.full_name}")
            print(f"{'Email:':<12}{user.email}")
            print(f"{'Number:':<12}{user.customer_number}")

        elif isinstance(user, Employee):
            print("\nEMPLOYEE")
            print(f"{'Name:':<12}{user.full_name}")
            print(f"{'Email:':<12}{user.email}")
            print(f"{'SSN:':<12}{user.SSN}")

        cont = input("\nContinue? (y/n): ")
        print()


if __name__ == "__main__":
    main()
    print("\nBye!")



