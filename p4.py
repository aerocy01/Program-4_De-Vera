def process_integers(filename):
    with open(filename, 'r') as file:
        integers = [int(line.strip()) for line in file.readlines()]

    even_numbers = []
    odd_numbers = []
    even_squares = []
    odd_cubes = []

    for integer in integers:
        if integer % 2 == 0:
            even_numbers.append(integer)
            even_squares.append(integer ** 2)
        else:
            odd_numbers.append(integer)
            odd_cubes.append(integer ** 3)

    print("Integers:")
    print(integers)

    print("Even numbers:")
    print(even_numbers)

    print("Odd numbers:")
    print(odd_numbers)

    print("Squares of even numbers:")
    print(even_squares)

    print("Cubes of odd numbers:")
    print(odd_cubes)

    with open('double.txt', 'w') as double_file:
        for square in even_squares:
            double_file.write(f"{square}\n")

    with open('triple.txt', 'w') as triple_file:
        for cube in odd_cubes:
            triple_file.write(f"{cube}\n")

    print("Processing completed. Check double.txt and triple.txt for results.")

# Call the method with the filename 'integers.txt'
process_integers('integers.txt')