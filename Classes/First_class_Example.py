from Class_Objects_1 import product


product_list = [product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                product("National Hardware 3/4' Wire Nails", 10.99, 25),
                product("Economy Duct Tape, 60 yds, silver", 6.99, 5)]


def title():
    print("The Product Viewer program\n")


def product_menu():
    print("PRODUCTS")
    print(f'1. {product_list[0].name}')
    print(f'2. {product_list[1].name}')
    print(f'3. {product_list[2].name}\n')


def main():
    title()
    loop = 'y'
    while loop == 'y':
        product_menu()
        product_num = int(input("Enter product number: ")) - 1
        print("\nPRODUCT DATA")
        print(f"Name:\t\t\t\t{product_list[product_num].name}")
        print(f"Price:\t\t\t\t{product_list[product_num].price:.2f}")
        print(f"Discount Percent:\t{product_list[product_num].discount:d}%")

        print(f"Discount Amount:\t{product_list[product_num].getDiscountAmount():.2f}")
        print(f"Discount Price:\t\t{product_list[product_num].getDiscountPrice():.2f}")
        loop = str(input("\nView another product? (y/n): ")).lower()


if __name__ == "__main__":
    main()
    print("\nBye!")
