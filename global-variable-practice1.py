# variables that are created OUTSIDE of a function
# global var - can be used by everyone, both inside and outside
# in this file, im just trying to know how global variable works

# Define global variables for length and width
length = 0
width = 0

def calculate_area():
    # Access the global variables inside the function
    global length, width
    area = length * width
    return area

def main():
    # Ask the user for the length and width of the rectangle
    global length, width
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate and print the area
    area = calculate_area()
    print("The area of the rectangle is:", area)

if __name__ == "__main__":
    main()
