import os
import img2pdf
import argparse


def get_images(path):
    # Get all JPG images from Directory
    return [i for i in os.listdir(path) if i.endswith(".jpg")]


def convert_images_to_pdf_data(images):
    # Convert image data to PDF
    return img2pdf.convert(images)


def write_pdf_file(pdf_file, data):
    # Write images to PDF file
    with open(pdf_file, "wb") as file:
        file.write(data)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file_name",
        help="Name of PDF file in Directory - e.g. output.pdf",
        default=None,
    )
    args = parser.parse_args()

    if args.file_name:
        pdf_file_name = args.file_name
    else:
        pdf_file_name = input("Please enter the name of your output PDF file (e.g. output.pdf): ")

    print("Fetching image files...")
    image_files = get_images("./")

    print("Converting images to PDF...")
    pdf_data = convert_images_to_pdf_data(image_files)

    print(f"Copying to {pdf_file_name}...")
    write_pdf_file(pdf_file_name, pdf_data)
    print(f"Successfully converted images to {pdf_file_name}.")


main()
