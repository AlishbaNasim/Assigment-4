
def main():
    fruit_prices = {
        "apple": 10.0,
        "durian": 30.0,
        "jackfruit": 25.0,
        "kiwi": 12.5,
        "rambutan": 7.0,
        "mango": 5.0
    }

    total_cost = 0.0

    for fruit, price in fruit_prices.items():
        quantity = input(f"How many ({fruit}) do you want?: ")
        if quantity.isdigit():  # ensure input is a number
            total_cost += int(quantity) * price
        else:
            print(f"Invalid input for {fruit}, assuming 0.")

    print(f"\nYour total is ${total_cost}")

if __name__ == "__main__":
    main()
