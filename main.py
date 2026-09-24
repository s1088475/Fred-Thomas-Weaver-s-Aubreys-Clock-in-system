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

def take_order(table_number, orders):
    print(f"Enter foods for Table {table_number}. Type 'done' when finished.")

    while True:
        food_name = input("Food: ").strip().lower()
        if food_name == "done":
            break
        elif food_name not in foods:
            print("That item is not on the menu.")
            continue
        elif not foods[food_name]['in_stock']:
            print("That item is currently out of stock.")
            continue
        orders.append(food_name)
        print(f"Added {food_name} to the order.")
    return orders


if __name__ == "__main__":
    table_orders = {}

    print("Enter a table number, or type 'quit' when finished.")

    while True:
        table_input = input("Table: ").strip().lower()

        if table_input == "quit":
            break

        if not table_input.isdigit() or int(table_input) < 1:
            print("Please enter a valid table number.")
            continue

        table_number = int(table_input)
        table_orders.setdefault(table_number, [])
        take_order(table_number, table_orders[table_number])

    print("\nAll table orders:")
    for table_number, orders in sorted(table_orders.items()):
        print(f"Table {table_number}: {orders}")