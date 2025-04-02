import pdfplumber

# Open the PDF file
with pdfplumber.open("../data/Gauteng_CPlanv4_Technical_Report_FINALv1_20240925.pdf") as pdf:
    # Loop through each page and extract text
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text()

# save the extracted text to a text file
with open("../data/extracted_text.txt", "w") as file:
    file.write(all_text)
