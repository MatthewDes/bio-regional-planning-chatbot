import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        return full_text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def convert_pdfs_to_txt(pdf_folder, txt_folder):
    """Converts all PDFs in pdf_folder to text files in txt_folder, skipping existing ones."""
    
    # Ensure the text folder exists
    os.makedirs(txt_folder, exist_ok=True)
    
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(txt_folder, txt_filename)
            
            # Skip if text file already exists
            if os.path.exists(txt_path):
                print(f"Skipping {filename}, already converted.")
                continue
            
            print(f"Processing {filename}...")
            text = extract_text_from_pdf(pdf_path)
            
            if text:
                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)
                print(f"Saved: {txt_path}")
            else:
                print(f"Warning: No text extracted from {filename}")

# Define folder paths
pdf_folder = "../data_pdf"
txt_folder = "../data_txt"

# Run the conversion
convert_pdfs_to_txt(pdf_folder, txt_folder)
