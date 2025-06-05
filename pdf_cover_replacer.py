import fitz  # PyMuPDF
from PIL import Image
import io
import os

def replace_pdf_cover(input_pdf_path, output_pdf_path, new_cover_path, insert_new_page=False):
    """
    Replace the cover (first page) of a PDF with a new image.
    
    Args:
        input_pdf_path (str): Path to the input PDF file
        output_pdf_path (str): Path to save the modified PDF
        new_cover_path (str): Path to the new cover image (PNG or JPG format)
        insert_new_page (bool): If True, inserts a new first page instead of replacing
    """
    # Open the PDF
    doc = fitz.open(input_pdf_path)
    
    # Get the dimensions from the first page
    first_page = doc[0]
    rect = first_page.rect
    
    if insert_new_page:
        # Insert a new first page with the same dimensions as the first page
        page = doc.new_page(0, width=rect.width, height=rect.height)
    else:
        # Use the first page and clear its content
        page = first_page
        page.clean_contents()
    
    # Add the new cover image
    img = Image.open(new_cover_path)
    
    # Determine the image format from the file extension
    img_format = 'PNG' if new_cover_path.lower().endswith('.png') else 'JPEG'
    
    # Convert image to RGB if it's RGBA and we're saving as JPEG
    if img.mode == 'RGBA' and img_format == 'JPEG':
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        img = background
    
    # Convert to bytes in the appropriate format
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=img_format)
    img_byte_arr = img_byte_arr.getvalue()
    
    # Calculate image rectangle to fit the page
    img_rect = fitz.Rect(0, 0, rect.width, rect.height)
    
    # Insert the image
    page.insert_image(img_rect, stream=img_byte_arr)
    
    # Save the modified PDF
    doc.save(output_pdf_path)
    doc.close()

if __name__ == "__main__":
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Replace or insert a cover page in a PDF.')
    parser.add_argument('input_pdf', help='Path to the input PDF file')
    parser.add_argument('output_pdf', help='Path to save the modified PDF')
    parser.add_argument('cover_image', help='Path to the new cover image (PNG or JPG format)')
    parser.add_argument('--insert', action='store_true', 
                       help='Insert a new first page instead of replacing the existing one')
    
    args = parser.parse_args()
    
    input_pdf = args.input_pdf
    output_pdf = args.output_pdf
    new_cover = args.cover_image
    insert_new_page = args.insert
    
    if not os.path.exists(input_pdf):
        print(f"Error: Input PDF file '{input_pdf}' not found.")
        sys.exit(1)
    
    if not os.path.exists(new_cover):
        print(f"Error: New cover image '{new_cover}' not found.")
        sys.exit(1)
        
    # Check if the file is either PNG or JPEG
    _, ext = os.path.splitext(new_cover.lower())
    if ext not in ['.png', '.jpg', '.jpeg']:
        print("Error: Cover image must be a PNG or JPEG file.")
        print("Supported formats: .png, .jpg, .jpeg")
        sys.exit(1)
    
    try:
        replace_pdf_cover(input_pdf, output_pdf, new_cover, insert_new_page)
        print(f"Successfully created new PDF with replaced cover: {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
