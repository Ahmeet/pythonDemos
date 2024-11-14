import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_directory(directory_path, output_pdf):
    # Create a PdfMerger object
    pdf_merger = PdfMerger()

    # List all files in the directory and filter PDF files
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):  # Only process .pdf files
            pdf_path = os.path.join(directory_path, filename)
            print(f'Merging: {pdf_path}')
            pdf_merger.append(pdf_path)

    # Write the merged PDF to the output file
    pdf_merger.write(output_pdf)
    pdf_merger.close()

    print(f'Merged PDF saved as {output_pdf}')

# Specify the directory where the PDF files are located
directory = r'C:\Users\intra\Desktop\vscode_workspace\pythonDemos\worldTemplateforWifi\worlds'  # Replace with your directory path
output_pdf = r'C:\Users\intra\Desktop\vscode_workspace\pythonDemos\worldTemplateforWifi\worlds\mergedOutput.pdf'  # Output PDF file

merge_pdfs_in_directory(directory, output_pdf)
