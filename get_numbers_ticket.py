import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = []
    if min < 1 :
        print("min must be greater than 0")
        return lottery_numbers
    if max > 1000:
        print("max must be less than 1000")
        return lottery_numbers
    if quantity < min or quantity > max:
        print("quantity must be between min and max")
        return lottery_numbers
    print(f"min: {min}, max: {max}, quantity: {quantity}")

    while quantity > 0:
        result = random.randint(min, max)
        if result not in lottery_numbers:
            lottery_numbers.append(result)
            quantity -= 1
    lottery_numbers.sort()
    print(f"Ваші лотерейні числа: {lottery_numbers}")

  

if __name__ == "__main__":
    get_numbers_ticket(1, 49, 6)
    get_numbers_ticket(1, 36, 5)