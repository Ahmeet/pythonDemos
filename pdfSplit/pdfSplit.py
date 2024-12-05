import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # Create an output folder to store split PDFs
    output_folder = os.path.join(folder_path, "split_pdfs")
    os.makedirs(output_folder, exist_ok=True)

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        pdf_reader = PdfReader(pdf_path)

        # Split each page
        for page_num, page in enumerate(pdf_reader.pages, start=1):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(page)

            # Create a new filename for the split page
            output_filename = f"{os.path.splitext(pdf_file)[0]}_{page_num}.pdf"
            output_path = os.path.join(output_folder, output_filename)

            # Write the split page to a new file
            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)

        print(f"Processed {pdf_file}, split into {len(pdf_reader.pages)} pages.")

    print(f"All files have been processed. Split PDFs are saved in: {output_folder}")

def main():
    folder_path = r"C:\Users\intra\Desktop\vscode_workspace\pythonDemos\pdfSplit\pdfs"
    split_pdf(folder_path)

# Example usage
if __name__ == "__main__":
    main()


