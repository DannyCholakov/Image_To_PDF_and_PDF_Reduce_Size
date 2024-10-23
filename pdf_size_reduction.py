import subprocess
import os
import tkinter as tk
from tkinter import filedialog

def compress_pdf(input_pdf_path, output_pdf_path, quality="screen"):
    """
    Compress a PDF using Ghostscript.

    :param input_pdf_path: The path to the input PDF file.
    :param output_pdf_path: The path to save the compressed PDF.
    :param quality: The quality setting for compression (options: 'screen', 'ebook', 'printer', 'prepress').
    """
    quality_settings = {
        "screen": "/screen",  # Low-resolution output
        "ebook": "/ebook",    # Medium-resolution output
        "printer": "/printer",  # High-resolution output
        "prepress": "/prepress"  # High-quality, large-size output
    }

    gs_command = [
        "gs", "-sDEVICE=pdfwrite",
        f"-dPDFSETTINGS={quality_settings.get(quality, '/screen')}",  # Default is 'screen'
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE", "-dQUIET", "-dBATCH",
        f"-sOutputFile={output_pdf_path}",
        input_pdf_path
    ]

    try:
        subprocess.run(gs_command, check=True)
        print(f"Compressed PDF saved as: {output_pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compress PDF: {e}")

def select_pdf():
    # Create a file dialog to select a PDF file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    input_pdf = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    return input_pdf

def main():
    print("Please select the PDF file to compress.")
    input_pdf = select_pdf()

    if not input_pdf:
        print("No PDF selected. Exiting.")
        return

    # Ask the user for the output PDF file name
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save Compressed PDF As")

    if not output_pdf:
        print("No output file specified. Exiting.")
        return

    # Ask for quality level
    quality = input("Enter quality level (screen, ebook, printer, prepress): ").strip().lower()

    # Compress the PDF
    compress_pdf(input_pdf, output_pdf, quality)

# Run the main function
if __name__ == "__main__":
    main()