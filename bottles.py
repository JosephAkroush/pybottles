#!/usr/bin/env python3

def main():
    while True:
        try:
            number_of_bottles = get_user_input()
        except ValueError:
            print("You must enter a valid number between 1-99")
            continue

        if number_of_bottles is None:
            break
        elif number_of_bottles < 1 or number_of_bottles > 99:
            print("You must enter a valid number between 1-99")
            continue

        print_lyrics(number_of_bottles)


def get_user_input():
    result = input("Enter a number between 1-99 or 'end' to end the program: ")
    if result == "":
        return 99
    elif result == "end":
        return None
    return int(result)


def print_lyrics(number_of_bottles):
    for num in range(number_of_bottles, -1, -1):
        if num > 2:
            print(f"{num} bottles of beer on the wall!")
            print(f"{num} bottles of beer!")
            print("Take one down")
            print("And pass it around")
            print(f"{num - 1} bottles of beer on the wall!")
            print()
        elif num == 2:
            print(f"{num} bottles of beer on the wall!")
            print(f"{num} bottles of beer!")
            print("Take one down")
            print("And pass it around")
            print(f"1 bottle of beer on the wall!")
            print()
        elif num == 1:
            print(f"{num} bottle of beer on the wall!")
            print(f"{num} bottle of beer!")
            print("Take one down")
            print("And pass it around")
            print(f"No more bottles of beer on the wall!")
            print()


if __name__ == "__main__":
    main()
