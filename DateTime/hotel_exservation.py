from datetime import datetime


def title():
    print("Hotel Hotel Reservation Program\n")


def calc_night_rate(arrival, departure):
    if 6 <= arrival.month <= 8:
        night_rate = float(105.00)
    else:
        night_rate = float(85.00)
    total_nights = (departure - arrival).days
    total_price = total_nights * night_rate
    return night_rate, total_nights, total_price


def main():
    title()
    while True:
        try:
            arrival = datetime.strptime(input('Enter arrival date (YYYY-MM-DD): '), "%Y-%m-%d")
            departure = datetime.strptime(input('Enter departure date (YYYY-MM-DD): '), '%Y-%m-%d')
            night_rate, total_nights, total_price = calc_night_rate(arrival, departure)
            print(f"\n{'Arrival Date:':<16}{arrival:%B %d, %Y}")
            print(f"{'Departure Date:':<16}{departure:%B %d, %Y}")
            if night_rate == 105.00:
                print(f"{'Nightly rate:':<16}${night_rate:.2f} (High season)")
            else:
                print(f"{'Nightly rate:':<16}${night_rate:.2f}")
            print(f"{'Total nights:':<16}{total_nights}")
            print(f"{'Total price:':<16}${total_price:.2f}")
        except ValueError:
            print('\nInvalid date of Arrival or Departure, Enter a valid date for both.\n')
            continue
        choice = input("\ncontinue? (y/n): ")
        if choice == 'y':
            continue
        elif choice == 'n':
            break


if __name__ == '__main__':
    main()
    print("\nBye!")
