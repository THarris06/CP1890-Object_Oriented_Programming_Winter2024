from datetime import datetime, timedelta


def title():
    print("The Invoice Due Date program\n")


def calc_dates(invoice_date, current_date):
    days_till = timedelta(days=30)
    due = invoice_date + days_till
    days_late = current_date - due
    return due, days_late


def main():
    title()
    while True:
        invoice_date = datetime.strptime(input("Enter the invoice date (MM/DD/YY): "), '%m/%d/%y')
        current_date = datetime.now()
        due_date, late = calc_dates(invoice_date, current_date)
        print(f"\n{'Invoice date:':13}{invoice_date: %B %d,%Y}")
        print(f"{'Due date:':13}{due_date: %B %d,%Y}")
        print(f"{'Current date:':13}{current_date: %B %d,%Y}")
        print(f"\nThis invoice is {late.days} day(s) overdue.")
        choice = input("\ncontinue? (y/n):")
        if choice == "y":
            continue
        elif choice == "n":
            break


if __name__ == "__main__":
    main()
