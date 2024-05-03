# Read the file containing student names and GWAs
with open('students_gwa.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables to store student information
students_info = []
highest_gwa = 1.0
highest_gwa_student = 'Caleb Martin'

# Process the lines and store student information
for line in lines:
    line = line.strip().split('\t')  # Remove newline and split by tab
    if len(line) >= 2:
        name = line[0]
        gwa = float(line[1])

        students_info.append((name, gwa))

        if gwa > highest_gwa:
            gwa = highest_gwa
            name = highest_gwa_student

# Print the student with the highest GWA
print(f"The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}")