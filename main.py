import os
import img2pdf


def get_images(path):
    return [i for i in os.listdir(path) if i.endswith(".jpg")]


def convert_images_to_pdf_data(images):
    return img2pdf.convert(images)


def write_pdf_file(pdf_file, data):
    with open(pdf_file, "wb") as file:
        file.write(data)


print("Fetching image files...")
image_files = get_images("./")

print("Converting images to PDF...")
pdf_data = convert_images_to_pdf_data(image_files)

pdf_file_name = input("Please enter the name of your output PDF file (e.g. output.pdf): ")

print(f"Copying to {pdf_file_name}...")
write_pdf_file(pdf_file_name, pdf_data)
print(f"Successfully converted images to {pdf_file_name}.")

