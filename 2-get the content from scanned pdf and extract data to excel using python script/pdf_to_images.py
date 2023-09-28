import os
import fitz  # PyMuPDF
import shutil

#pure function
def pdfToImages(pdf_file,output_directory):
    try:
        #check the cropped_images folder exists, if then delete it
        if os.path.exists(output_directory):
            # os.rmdir(output_directory)
            shutil.rmtree(output_directory)
            os.makedirs(output_directory)
        else:
            os.makedirs(output_directory)

        # Open the PDF file
        pdf_document = fitz.open(pdf_file)

        # Iterate through each page and convert to an image
        for page_number in range(len(pdf_document)):
            # Get the page
            page = pdf_document[page_number]

            # Convert the page to an image (PNG format)
            pix = page.get_pixmap()

            # Save the image to a file
            image_file = f"page_{page_number + 1}.png"
            pix.save(os.path.join(output_directory,image_file), "png")

        # Close the PDF document
        pdf_document.close()
        return True
    except:
        return False



 
# # Output directory where images will be saved
# output_directory = r'temp_images'

# # Input PDF file path
# pdf_file = r'input.pdf'

# status = pdfToImages(pdf_file,output_directory)
# print(status)




