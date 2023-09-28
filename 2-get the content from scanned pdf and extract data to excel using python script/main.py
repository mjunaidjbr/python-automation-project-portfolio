from pdf_to_images import pdfToImages
from crop_images import cropImages
from get_text_from_image import getTextFromImage
import os
import shutil
pdfs_folder=r"C:\Users\rao\Desktop\Freelance\python_scripts\python Automation scripts\project_script_29\pdf_data_extraction\pdfs"
pdf_images_temporary_Folder = os.path.join(os.path.dirname(__file__), "temp_pdf_images")
cropped_images_temporary_Folder = os.path.join(os.path.dirname(__file__), "temp_cropped_images")

#get all pdf files from pdfs folder
all_pdf_files = [os.path.join(pdfs_folder,pdf_file) for pdf_file in os.listdir(pdfs_folder)]
for pdf_file in all_pdf_files[0:1]:
    status1 = pdfToImages(pdf_file=pdf_file,output_directory=pdf_images_temporary_Folder)
    if status1 == False:
        print(f"issue while processing {pdf_file} | while converting pdf to images ")
        continue

    all_pdf_images_files = [os.path.join(pdf_images_temporary_Folder,image_file) for image_file in os.listdir(pdf_images_temporary_Folder)]
    for page_number,image_file in enumerate(all_pdf_images_files):
        status2 = cropImages(image_path=image_file,folder_path=cropped_images_temporary_Folder)
        if status2 == False:
            print(f"issue while processing pdf: {pdf_file} page number: {page_number} | while converting pdf page to cropped images ")
            continue 
        else:
            all_pdf_cropped_images_files = [os.path.join(cropped_images_temporary_Folder,image_file) for image_file in os.listdir(cropped_images_temporary_Folder)]
            if os.path.exists(os.path.join(cropped_images_temporary_Folder,"piece_0.png")):
                text = getTextFromImage(os.path.join(cropped_images_temporary_Folder,"piece_0.png"))
                if text != None:
                    print(text)
                    print("--------------------------------")
                    # try:
                    #     if "વિધાનસભા મત વિભાગનો નંબર અને નામ" in text:
                    #         text1 = text.strip().split("\n")[0]
                    #         text2 = text1.split(":")[1]
                    #         print(str(text2))
                    # except:
                    #     print("issue in filter")
                    
                
                    
                    
                    try:
                        with open(os.path.join(os.getcwd(),"temp1.txt"), "w",encoding='utf8') as temp:
                            temp.write(str(text.strip().replace("\n\n", "")))
                        text_read_list = open(os.path.join(os.getcwd(),"temp1.txt"),encoding='utf8').readlines()
                        # print(text_read_list)
                        for text_read in text_read_list:
                            if "વિધાનસભા મત વિભાગનો નંબર અને નામ" in text_read:
                                if "નામ" in text_read:
                                    text1 = text_read.strip().split("\n")[0]
                
                                    text1_ = text1.split(":")[1]
                                    text2 = text1_.split("નામ")[1]
                                    print(f"category detected: {str(text2.strip())}")
                                    print("##############################")
                                    try:
                                        if not os.path.exists(os.path.join(os.path.dirname(__file__),"category_data",text2.strip())):
                                            os.makedirs(os.path.join(os.path.dirname(__file__),"category_data",text2.strip()))
                                        #check the number of files in os.path.join(os.path.dirname(__file__),"category_data",text2.strip()) folder
                                        count = len(os.listdir(os.path.join(os.path.dirname(__file__),"category_data",text2.strip())))
                                        #move all files to new directory
                                        for item in all_pdf_cropped_images_files:
                                            shutil.move(item,os.path.join(os.path.join(os.path.dirname(__file__),"category_data",text2.strip()),f"{count}.png"))
                                            count = count + 1
                                    except:
                                        print("Error while moving files to new directory")
                                    if os.path.exists(os.path.join(os.getcwd(),"temp1.txt")):
                                        os.remove(os.path.join(os.getcwd(),"temp1.txt"))
                                    break
                    except:
                        if os.path.exists(os.path.join(os.getcwd(),"temp1.txt")):
                            os.remove(os.path.join(os.getcwd(),"temp1.txt"))
                        # print("issue in filter")
                        print(f"issue while processing pdf: {pdf_file} page number: {page_number} | while category filtering ")

        shutil.rmtree(cropped_images_temporary_Folder)            
                    
    shutil.rmtree(pdf_images_temporary_Folder)                    
                    
                
