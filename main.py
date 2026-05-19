def calculate_total(price, quantity, percentageTax=0, percentageDiscount =0):
    total = price * quantity
    total += total * percentageTax / 100
    total -= total * percentageDiscount / 100
    return total

def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity, 10, 10)
    print(f"Total amount: {total}")


main()