print("Welcome Customer")

name = input("Enter your name: ")

print("--- Our Menu ---")
print("1: Coffee Latte (Rp 30.000)")
print("2: Cappuccino (Rp 35.000)")
print("3: Green Tea (Rp 28.000)")

drink = int(input("Enter your drink: "))

coffee_latte = 30000
cappuccino = 35000
greentea = 28000

match drink:
    case 1:
        quantity = int(input("Enter your quantity: "))
        price = coffee_latte * quantity

        member = input("Are you a member? ").lower()
        if member in ["yes", "y", "ya", "true"] and price >= 50000:
            discount = price * 0.1
            final_price = price - discount

            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} coffee latte after getting {discount} discount for being a member.')
        else:
            final_price = price
            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} coffee latte.')
    case 2:
        quantity = int(input("Enter your quantity: "))
        price = cappuccino * quantity

        member = input("Are you a member? ").lower()
        if member in ["yes", "y", "ya", "true"] and price >= 50000:
            discount = price * 0.1
            final_price = price - discount

            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} cappuccino after getting {discount} discount for being a member.')
        else:
            final_price = price
            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} cappuccino.')
    case 3:
        quantity = int(input("Enter your quantity: "))
        price = greentea * quantity

        member = input("Are you a member? ").lower()
        if member in ["yes", "y", "ya", "true"] and price >= 50000:
            discount = price * 0.1
            final_price = price - discount

            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} greentea after getting {discount} discount for being a member.')
        else:
            final_price = price
            print(f'Thanks {name}! Your final price is ${final_price} for {quantity} greentea.')
    case _:
        print(f'Sorry {name} the drink you want isn\'t available.')