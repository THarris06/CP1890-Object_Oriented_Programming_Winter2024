
from datetime import datetime
import locale as lc
lc.setlocale(lc.LC_ALL, 'en_CA')


'''Code of getting all Locale codes
   for loc in locale.locale_alias:
      print(loc)'''


def title():
    print("Hotel Hotel Reservation Program\n")


def get_arrival():
    while True:
        try:
            arrival_date = datetime.strptime(input('Enter arrival date (YYYY-MM-DD): '), "%Y-%m-%d")
        except ValueError as ve:
            print('\nInvalid date of Arrival , Enter a valid date.\n')
            print(f"Error:{ve}")
            continue
        now = datetime.now()
        if arrival_date < now:
            print("This date has pasted, arrival date needs to be today or later.\n")
        else:
            return arrival_date


def get_departure(arrival):
    while True:
        try:
            departure_date = datetime.strptime(input('Enter departure date (YYYY-MM-DD): '), "%Y-%m-%d")
        except ValueError as ve:
            print('\nInvalid date of departure , Enter a valid date.\n')
            print(f"Error:{ve}\n")
            continue
        if departure_date < arrival:
            print("This date has pasted your arrival, date needs to be later then arrival.\n")
        else:
            return departure_date


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
        arrival = get_arrival()
        departure = get_departure(arrival)
        night_rate, total_nights, total_price = calc_night_rate(arrival, departure)
        print(f"\n{'Arrival Date:':<16}{arrival:%B %d, %Y}")
        print(f"{'Departure Date:':<16}{departure:%B %d, %Y}")
        if night_rate == 105.00:
            print(f"{'Nightly rate:':<16}{lc.currency(night_rate, symbol=True, grouping=True)} (High season)")
        else:
            print(f"{'Nightly rate:':<16}${lc.currency(night_rate, symbol=True, grouping=True)}")
        print(f"{'Total nights:':<16}{total_nights}")
        print(f"{'Total price:':<16}{lc.currency(total_price, symbol=True, grouping=True)}")

        choice = input("\ncontinue? (y/n): ")
        if choice == 'y':
            continue
        elif choice == 'n':
            break


if __name__ == '__main__':
    main()
    print("\nBye!")
