import locale as lc


def get_values():
    invest = float(input("\nEnter the investment:\t\t "))
    rate = float(input("Enter Yearly interest rate:\t "))
    years = int(input("Enter number of years:\t\t "))
    return invest, rate, years


def calculate_values(invest, rate, years):
    future_value = 0
    for i in range(years*12):
        future_value += invest
        monthly = future_value * (rate/(12*100))
        future_value += monthly
    return future_value


def main():
    print('Future Value Calculator')
    loop = 'y'
    while loop == 'y':
        invest, rate, years = get_values()
        calculated_value = calculate_values(invest, rate, years)
        lc.setlocale(lc.LC_ALL, 'en-ca')
        print(f"\nmonthly investment:{lc.currency(invest, grouping=True):>13}")
        print(f"Interest rate:{rate:>18}")
        print(f"Years:{years:>26}")
        print(f"Future value:{lc.currency(calculated_value, grouping=True):>19}")
        loop = input("\ncontinue? (y/n): ")


if __name__ == '__main__':
    main()
