def max_rectangle_area(base, height):
    # Calculate the base and height of the rectangle
    b = base / 2
    h = height - (height * b) / base

    # Calculate the maximum area
    max_area = b * h

    return max_area

# Get the base and height of the isosceles triangle from the user
base = float(input("Enter the base of the isosceles triangle: "))
height = float(input("Enter the height of the isosceles triangle: "))

# Calculate and print the maximum possible area of the rectangle
max_area = max_rectangle_area(base, height)
print(f"The maximum possible area of a rectangle that can be placed inside the triangle is {max_area} square units.")
