import os

def write_to_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

    with open(filename, 'a') as file:
        while True:
            line = input("Enter line: ")
            file.write(f"{line}\n")

            continue_writing = input("Are there more lines y/n? ")
            if continue_writing.lower() != 'y':
                break

    print("Writing completed.")

# Call the method with the filename 'mylife.txt'
write_to_file('mylife.txt')

