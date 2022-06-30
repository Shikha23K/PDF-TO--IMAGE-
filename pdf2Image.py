from pdf2image import convert_from_path

import os

# Define the location of the directory
path =r"D:/sheelu data/doc"

# Change the directory
os.chdir(path)

def read_files(file_path):
   with open(file_path, 'r') as file:
      print(file.read())

# Iterate over all the files in the directory
for file in os.listdir():
   if file.endswith('.pdf'):
        # Create the filepath of particular file
        pdf_file =f"{path}/{file}"              

    #let conversion begine

        pages=convert_from_path(pdf_file)

        #replace .pdf to a blank so that we can add to extension while saving it
        img_file=pdf_file.replace(".pdf","")

        #saving pages in TIFF format

        count=0
        for page in pages:
            count+=1
            jpeg_file=img_file+"-"+str(count)+".tiff"
            page.save(jpeg_file,'TIFF')

