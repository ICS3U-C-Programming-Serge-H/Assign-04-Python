#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program will ask you for a positive integer, then multiply that number by 0 to 10.


def main():
    while True:
        try:
            # Get a positive number from the user.
            user_number = int(input("Enter a whole number: "))
            print("")

            # Multiply user_number from 0 to 10.
            if user_number > 0:
                break
            else:
                print("Invalid. Enter a positive number")
        except ValueError:
            print("Invalid. Enter a whole number")

    # Here is where initialization starts

    print(f"\nMultiplication Table for {user_number}:")

    counter = 0
    for counter in range(11):
        product = user_number * counter
        print(f"{user_number} x {counter} = {product}")

        # This is the nested statement which i have added
        if product > 50:
            print("That's a big product!")

        counter += 1

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
