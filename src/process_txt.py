import re

def extract_table_of_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    toc_start = None
    toc_entries = {}
    
    pattern = re.compile(r'^([\w \:\.\(\)]*) ([\.]+) ([0-9]+)|^([0-9\.]+)')

    for i, line in enumerate(lines):
        if re.search(r'(Table of Contents|Contents)', line, re.IGNORECASE):
            toc_start = i
            break  # Stop at the first occurrence

    if toc_start is None:
        return "No Table of Contents found."

    # Extract ToC using the regex pattern
    for line in lines[toc_start + 2:]:
        # if re.match(pattern, line.strip()):
        #     toc_lines.append(line.strip())
        match = pattern.match(line.strip())
        if match:
            section_number = match.group(4)        # Main or sub-section number
            title = match.group(1)                 # Section title
            page_number = match.group(3)           # Page number

            if section_number:
                last_section_number = section_number  # Store section number
            elif title and page_number:
                formatted_entry = f"{last_section_number} {title}"   # Format the entry
                cleaned_section = str(last_section_number).replace('.', '')   # Ensure last_section_number is a string
                if len(cleaned_section) == 1:
                    toc_entries[formatted_entry] = {"page": page_number}
                    previous_title = formatted_entry
                elif len(cleaned_section) == 2:
                    toc_entries[previous_title][formatted_entry] = {"page": page_number}
                    previous_subtitle = formatted_entry
                elif len(cleaned_section) == 3:  
                    toc_entries[previous_title][previous_subtitle][formatted_entry] = {"page": page_number}

                last_section_number = ""  # Reset after use
            
        elif len(line.strip()) == 0:  # Stop at an empty line (possible end of ToC)
            break

    return toc_entries if toc_entries else "No structured ToC found."

# Example usage
file_path = "../data_txt/CITY OF EKURHULENI BIOREGIONAL PLAN 2020 Technical Report 20210603.txt"
toc = extract_table_of_contents(file_path)
for key, value in toc.items():
    print(f"{key}: {value}")
