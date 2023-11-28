#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 28th, 2023
# This program asks the user for the base and height in cm
# then calculates and displays the area of the triangle


def calc_area(base, height):
    # Calculate the area
    area = base * height / 2

    # Display the area of the triangle
    print("The area of the triangle is {:.2f}cm².".format(area))


def main():
    # get base and height from the user
    base_str = input("Enter the base (cm): ")
    height_str = input("Enter the height (cm): ")

    # Make sure the base and height are floats using a nested try
    try:
        base_float = float(base_str)
        try:
            height_float = float(height_str)

            # Check if the base and height are less than or equal to 0
            if base_float <= 0:
                print("{} is not a valid base.".format(base_float))
            elif height_float <= 0:
                print("{} is not a valid height.".format(height_float))
            else:
                # Call function to calculate area
                calc_area(base_float, height_float)
        except:
            # Height is not a float
            print("{} is not a number.".format(height_str))
    except:
        # Base is not a float
        print("{} is not a number.".format(base_str))


if __name__ == "__main__":
    main()
