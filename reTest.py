import re

# Input string
text = "'K9 48.72▼D9 62.63▼J9 90.43▲3K-2D 20.92▼RSV 0.00▼'"

# Regular expression to match the float value "48.72"
# match = re.search(r'\b48\.72\b', text)
# match = re.search(r'\b\d+\.\d+\b', text)
match = re.search(r'K9\s+(\d+\.\d+)', text)

# Check if a match was found and print it
if match:
    print("Found:", match.group(1))
else:
    print("No match found.")