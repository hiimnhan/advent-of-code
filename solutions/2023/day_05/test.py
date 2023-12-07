
# Function to extract numbers from a line
def extract_numbers(line):
    return [int(num) for num in line.split() if num.isdigit()]

# Function to extract numbers under a specific section
def extract_numbers_under_section(content, section_name):
    numbers_array = []
    in_section = False

    for line in content:
        # Check if the line contains the specified section name
        if section_name in line:
            in_section = True
            continue

        # Check if we are in the specified section
        if in_section:
            # Check if the line contains numbers
            if any(char.isdigit() for char in line):
                # Extract numbers from the line and append to the array
                numbers_array.extend(extract_numbers(line))
            else:
                # If the line doesn't contain numbers, we are done with the section
                break

    return numbers_array

# Read the content of the file
file_path = "input.test.txt"  # Replace with the actual path to your file
with open(file_path, 'r') as file:
    content = file.readlines()

# Specify the section name you want to extract numbers from
section_name = "soil-to-fertilizer map:"

# Extract numbers under the specified section
numbers_under_section = extract_numbers_under_section(content, section_name)

# Print the resulting array
print(numbers_under_section)
