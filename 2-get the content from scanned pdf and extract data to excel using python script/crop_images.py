from PIL import Image
import os
import shutil


def cropImages(image_path,folder_path):
    try:
        #check the cropped_images folder exists, if then delete it
        if os.path.exists(folder_path):
            # os.rmdir(folder_path)
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
        else:
            os.makedirs(folder_path)

        original_image = Image.open(image_path)

        # Get the dimensions of the original image
        width, height = original_image.size

        # Define the height of each cropped piece (50 pixels in this case)
        piece_height = 25

        # Calculate the number of pieces that can fit in the Y-axis
        num_pieces = height // piece_height

        # Crop and save each piece
        for i in range(num_pieces):
            if i == 0:
                top = 0
                bottom = piece_height
            else:
                piece_height = 79
                top = 25 + piece_height*(i-1) 
                if top > 820:
                    break
                bottom = 25 + piece_height*(i) 

            # Crop the piece
            piece = original_image.crop((0, top, width, bottom))

            # Save the piece as a separate image
            piece.save(os.path.join(folder_path, f"piece_{i}.png"))

        # Close the original image
        original_image.close()
        return True
    except:
        return False


# # Open the image file
# image_path = r"temp_images\page_13.png"
# folder_path = r"cropped_images"
# status = cropImages(image_path, folder_path)
# print(status)