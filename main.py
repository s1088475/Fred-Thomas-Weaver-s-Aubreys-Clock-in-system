foods = {
    # Specialties
    'chicken finger platter': {'price': 16.00, 'in_stock': True},
    'buttermilk fried chicken': {'price': 18.00, 'in_stock': True},
    'fish and chips': {'price': 18.00, 'in_stock': True},
    'north carolina catfish': {'price': 16.00, 'in_stock': True},
    'boston scrod': {'price': 18.00, 'in_stock': True},

    # Favorites
    'citrus glazed salmon': {'price': 26.00, 'in_stock': True},
    'lemon lime chicken': {'price': 16.00, 'in_stock': True},
    'hickory chicken': {'price': 18.00, 'in_stock': True},
    'steak on a stick': {'price': 24.00, 'in_stock': True},
    'center cut sirloin': {'price': 24.00, 'in_stock': True},
    'ribeye 12oz': {'price': 30.00, 'in_stock': True},
    'ribeye 16oz': {'price': 40.00, 'in_stock': True},
    'hawaiian ribeye': {'price': 39.00, 'in_stock': True},
    'filet mignon 6oz': {'price': 34.00, 'in_stock': True},
    'filet mignon 9oz': {'price': 42.00, 'in_stock': True},

    # Pasta
    'haystack pasta': {'price': 18.00, 'in_stock': True},
    'tomato basil': {'price': 17.00, 'in_stock': True},
    'rattlesnake pasta': {'price': 18.00, 'in_stock': True},
    'seafood pasta': {'price': 17.00, 'in_stock': True},

    # Drinks - wine
    'banfi maschio prosecco': {'price': 7.00, 'in_stock': True},
    'klinker brick bricks roses rose': {'price': 9.00, 'in_stock': True},
    'schmitt sohne relax riesling': {'price': 8.00, 'in_stock': True},
    'benvolio pinot grigio': {'price': 8.00, 'in_stock': True},
    'kim crawford sauvignon blanc': {'price': 10.00, 'in_stock': True},
    'rodney strong chardonnay': {'price': 7.00, 'in_stock': True},
    'mer soleil silver chardonnay': {'price': 10.00, 'in_stock': True},
    'wente bailey hill pinot noir': {'price': 8.00, 'in_stock': True},
    'rodney strong russian river pinot noir': {'price': 10.00, 'in_stock': True},
    'j lohr merlot': {'price': 10.00, 'in_stock': True},
    'gundlach bundschu mountain cuvee': {'price': 11.00, 'in_stock': True},
    'elou red blend': {'price': 9.00, 'in_stock': True},
    'conundrum red blend': {'price': 10.00, 'in_stock': True},
    'rodney strong cabernet sauvignon': {'price': 12.00, 'in_stock': True},
    'serial cabernet sauvignon': {'price': 10.00, 'in_stock': True}
}

def calculate_total(orders):
    return sum(foods[item]['price'] for item in orders)


def show_orders(orders):
    if not orders:
        print("No items ordered.")
        return

    print("\nCurrent order:")
    for number, item in enumerate(orders, start=1):
        print(f"{number}. {item} - ${foods[item]['price']:.2f}")
    print(f"Total: ${calculate_total(orders):.2f}")


def take_order(table_number, orders):
    print(f"Enter foods for Table {table_number}.")
    print("Type 'show' to view items, 'delete' to remove an item, or 'done' when finished.")

    while True:
        food_name = input("Food: ").strip().lower()

        if food_name == "done":
            break

        if food_name == "show":
            show_orders(orders)
            continue

        if food_name == "delete":
            show_orders(orders)
            if orders:
                try:
                    item_number = int(input("Enter item number to delete: "))
                    if 1 <= item_number <= len(orders):
                        removed_item = orders.pop(item_number - 1)
                        print(f"Deleted {removed_item}.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")
            continue

        if food_name not in foods:
            print("That item is not on the menu.")
            continue

        if not foods[food_name]['in_stock']:
            print("That item is currently out of stock.")
            continue

        orders.append(food_name)
        print(f"Added {food_name} to the order.")

    return orders


def show_all_orders(table_orders):
    if not table_orders:
        print("No table orders yet.")
        return

    print("\nAll table orders:")
    for table_number, orders in sorted(table_orders.items()):
        print(f"Table {table_number}: {orders} - Total: ${calculate_total(orders):.2f}")


def show_status(table_orders):
    if not table_orders:
        print("No tables are currently open.")
        return

    print("\nTable status:")
    for table_number, orders in sorted(table_orders.items()):
        status = "Open" if orders else "Empty"
        print(
            f"Table {table_number}: {status} - "
            f"{len(orders)} item(s) - ${calculate_total(orders):.2f}"
        )


def get_table_number():
    table_input = input("Table number: ").strip()
    if not table_input.isdigit() or int(table_input) < 1:
        print("Please enter a valid table number.")
        return None
    return int(table_input)


if __name__ == "__main__":
    table_orders = {}

    while True:
        print("\n=== Aubrey's Order Taking System ===")
        print("1. New Order")
        print("2. View Orders")
        print("3. Update Order")
        print("4. Status")
        print("5. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice in {"5", "quit", "q"}:
            break

        if choice == "1":
            table_number = get_table_number()
            if table_number is None:
                continue
            table_orders.setdefault(table_number, [])
            take_order(table_number, table_orders[table_number])
        elif choice == "2":
            show_all_orders(table_orders)
        elif choice == "3":
            table_number = get_table_number()
            if table_number is None:
                continue
            if table_number not in table_orders:
                print("That table does not have an order yet.")
                continue
            take_order(table_number, table_orders[table_number])
        elif choice == "4":
            show_status(table_orders)
        else:
            print("Please choose an option from 1 to 5.")

    if table_orders:
        print()
        show_all_orders(table_orders)