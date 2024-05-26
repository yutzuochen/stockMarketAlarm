import re

# Input string
input_string = "K(9,3) 87.51%D(9,3) 84.87%"

# Regular expression pattern to match "87" before "%"
# pattern = r'K\(9,3\) \d+\.\d+%'
# pattern = r'\bK\(9,3\) (\d+\.\d+%)'
pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'


# Search for the pattern in the input string
match = re.search(pattern, input_string).group(1)

# Check if a match is found and print the result
if match:
    result = match.group(1)
    print("Matched value:", result)
else:
    print("No match found")