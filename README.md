# combine-images-to-pdf

Python script to convert multiple images into a single PDF file.

## What does it do?

This script takes all the jpg image files in the directory, and writes them to an existing PDF file in the directory.

## Installation:

You need to import the relevant 2 packages/modules/libraries named os and img2pdf.

```
import os
import img2pdf
```

## Options:
Run the script with a combination of the available arguments:

`--file_name` - The filename used for the export (if you don't provide one, the script will ask)

## Example:

Export a images to a PDF file called "output.pdf":

`python3 main.py --file_name output.pdf`

