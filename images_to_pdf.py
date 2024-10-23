from fpdf import FPDF
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def images_to_pdf(image_paths, output_pdf_path):
    # Initialize PDF object
    pdf = FPDF()

    # Loop through each image path
    for image_path in image_paths:
        # Open the image to get its dimensions
        img = Image.open(image_path)
        width, height = img.size

        # Convert pixels to mm (1px = 0.264583 mm)
        width_mm, height_mm = width * 0.264583, height * 0.264583

        # Calculate scaling ratio to fit the image on an A4 page
        A4_width, A4_height = 210, 297  # A4 size in mm
        scale = min(A4_width / width_mm, A4_height / height_mm)

        # Calculate the new dimensions for the image
        new_width_mm = width_mm * scale
        new_height_mm = height_mm * scale

        # Calculate margins to center the image
        x_offset = (A4_width - new_width_mm) / 2
        y_offset = (A4_height - new_height_mm) / 2

        # Add a new page to the PDF
        pdf.add_page()

        # Insert the image on the page with the calculated offsets
        pdf.image(image_path, x_offset, y_offset, new_width_mm, new_height_mm)

    # Save the PDF to the specified path
    pdf.output(output_pdf_path)
    print(f"PDF created successfully: {output_pdf_path}")


def select_images():
    # Create a file dialog to select multiple image files
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    image_files = filedialog.askopenfilenames(title="Select Image Files",
                                              filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
    return list(image_files)


def main():
    print("Please select the image files to create the PDF.")
    image_files = select_images()

    if not image_files:
        print("No images selected. Exiting.")
        return

    # Ask the user for the output PDF file name
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")],
                                              title="Save PDF As")

    if output_pdf:
        images_to_pdf(image_files, output_pdf)
    else:
        print("No output file specified. Exiting.")


# Run the main function
if __name__ == "__main__":
    main()