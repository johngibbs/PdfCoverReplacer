# PDF Cover Replacer

A Python script to replace the cover (first page) of a PDF file with a new image.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- venv (included in standard Python installation)

## Installation

1. Clone this repository or download the script
2. Create and activate a virtual environment (optional):

    **Note:** Using a virtual environment is strongly recommended to avoid conflicts with other Python projects.

    First, create a new virtual environment:

    ```bash
    python -m venv venv
    ```

    Then activate it based on your operating system and shell:

    For Windows PowerShell:
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

    For Windows Command Prompt:
    ```cmd
    venv\Scripts\activate.bat
    ```

    For Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

3. Finally, install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python pdf_cover_replacer.py <input_pdf> <output_pdf> <cover_image>
```

### Parameters

- `input_pdf`: Path to the input PDF file
- `output_pdf`: Path where the modified PDF will be saved
- `cover_image`: Path to the new cover image (PNG or JPG/JPEG format)

### Example

```bash
python pdf_cover_replacer.py input.pdf output_with_new_cover.pdf cover_image.png
```

## Features

- Replaces the first page of the PDF with the specified image
- Preserves the original PDF's page dimensions
- Simple command-line interface with error handling

## Notes

- The script will overwrite the output file if it already exists
- The new cover image will be scaled to fit the original PDF's first page dimensions
- For best results, use an image with similar dimensions to the PDF page
