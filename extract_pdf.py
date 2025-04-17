import PyPDF2
import os
import json

def extract_pdf_content(pdf_path):
    """Extract text content from PDF file"""
    content = []
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            print(f"Total pages in PDF: {num_pages}")
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    content.append({
                        "page": page_num + 1,
                        "text": text
                    })
                    print(f"Extracted content from page {page_num + 1}")
                else:
                    print(f"No text content found on page {page_num + 1}")
        
        # Save the extracted content to a JSON file
        output_path = os.path.join(os.path.dirname(pdf_path), "pdf_content.json")
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(content, json_file, indent=2, ensure_ascii=False)
        
        print(f"Content saved to {output_path}")
        return True
    
    except Exception as e:
        print(f"Error extracting PDF content: {str(e)}")
        return False

if __name__ == "__main__":
    pdf_path = "/home/ubuntu/upload/DT42 deck 2020 (AIKEA focus).pdf"
    success = extract_pdf_content(pdf_path)
    
    if not success:
        print("Attempting to get PDF information...")
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                print(f"PDF Information:")
                print(f"Number of pages: {len(reader.pages)}")
                if reader.metadata:
                    for key, value in reader.metadata.items():
                        print(f"{key}: {value}")
        except Exception as e:
            print(f"Error getting PDF information: {str(e)}")
