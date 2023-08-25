import os
import img2pdf

directory_path = input("Please enter the path of the directory containing your JPEG images: ")
pdf_file_name = input("Please give your PDF file a name (e.g. output.pdf): ")

image_files = [i for i in os.listdir(directory_path) if i.endswith(".jpg")]

pdf_data = img2pdf.convert(image_files)

with open("output.pdf", "wb") as file:
    file.write(pdf_data)
