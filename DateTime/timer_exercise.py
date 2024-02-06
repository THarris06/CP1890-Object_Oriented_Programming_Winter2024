import datetime


def title():
    print("The Timer program\n")


def timer():
    input("Press Enter to start...")
    start_time = datetime.datetime.now()
    print(f"Start time: {start_time}")
    input("\nPress Enter to stop...")
    end_time = datetime.datetime.now()
    print(f"Stop time: {end_time}")
    elapsed_time = end_time - start_time
    print("\nELAPSED TIME")
    print(f"Time: {elapsed_time}")


def main():
    title()
    timer()


if __name__ == "__main__":
    main()