import markdown
from weasyprint import HTML

def markdown_to_pdf(input_md, output_pdf):
    """
    Converts a Markdown file to a PDF.
    
    Args:
        input_md (str): Path to the input Markdown file.
        output_pdf (str): Path to the output PDF file.
    """
    try:
        # Read the Markdown file
        with open(input_md, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Convert HTML to PDF
        HTML(string=html_content).write_pdf(output_pdf)

        print(f"PDF successfully created at: {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
markdown_to_pdf("example.md", "output.pdf")
