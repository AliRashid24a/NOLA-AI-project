import re
from datetime import datetime

def combined_parser(text: str) -> str:
    # First try to parse the names associated with digits
    names = parse_name_identifier(text)
    # If no names were found using the first method, try using the address method
    if not names:
        names = parse_name_address(text)
    return clean_string(names)

def parse_name_address(text: str):
    # Define a regex pattern to detect lines starting with numbers (address)
    address_pattern = re.compile(r'^\d+.*$', re.MULTILINE)
    # Split the text at the address part
    parts = address_pattern.split(text, 1)
    # Check if we have the expected parts
    if len(parts) > 1:
        # Extract the part before the address
        before_address = parts[0].strip()
        # Extract the two strings before the address
        lines = before_address.split('\n')
        two_strings_before_address = lines[-2:]
        # Ensure we have exactly two lines
        if len(two_strings_before_address) == 2:
            return f"{two_strings_before_address[0]} {two_strings_before_address[1]}"
        else:
            raise ValueError("Unable to extract name before the address.")
    else:
        raise ValueError("Address not found in the text.")

def parse_name_identifier(text: str):
    # Define a regex pattern to find lines that start with digits followed by a name
    name_pattern = re.compile(r'\b\d+([A-Z]+)\s*/?\s*\n?\b\d+([A-Z]+)', re.MULTILINE | re.IGNORECASE)
    
    # Search for the pattern in the text
    match = name_pattern.search(text)
    
    # If a match is found, extract the names
    if match:
        name1 = match.group(1).strip()
        name2 = match.group(2).strip()
        return f"{name1} {name2}"
    #else:
        #raise ValueError("Names not found in the text.")

def clean_string(input_string: str) -> str:
    # Remove commas
    cleaned_string = input_string.replace(',', '')
    # Remove extra spaces
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
    return cleaned_string

def check_if_valid(text: str) -> None:
    # Get dates from text and checks if they are valid
    dates_str = get_dates(text)
    valid = isValid(dates_str)

    print(f'Expiration Date: {valid[0]}')
    if valid[1] == False:
        print('Warning: Expired')
    else:
        print('Accepted')
    
def get_dates(text: str) -> list[str]:
    # Regular expression to find dates in MM/DD/YYYY format
    date_pattern = r'\b\d{2}[/-]\d{2}[/-]\d{2,4}\b'
    # Find all matches
    dates = re.findall(date_pattern, text)
    return dates

def parse_date(date_string: str):
    # List of possible date formats
    date_formats = ['%m/%d/%Y', '%m-%d-%Y', '%m/%d/%y', '%m-%d-%y'] 
    # Parse through date_formats to find the correct one
    for fmt in date_formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
            
def isValid(dates_str: list[str]) -> tuple[str, bool]:
    # Parse dates and filter out None values
    dates = [parse_date(date) for date in dates_str if parse_date(date) is not None]
    # expiration date will be the greatest date in the text
    expiration_date = max(dates)
    # Convert the greatest date back to a string
    expiration_date_str = expiration_date.strftime('%m/%d/%Y')

    today = datetime.now()
    # Compare today's date with the greatest date to determine valdity
    if today > expiration_date:
        return (expiration_date_str, False)
    else:
        return (expiration_date_str, True)
    