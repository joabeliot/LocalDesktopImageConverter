import sys
import os
from tkinter import *
from PIL import Image, ImageTk
import pillow_avif

def isImg(filename):
    try:
        img = Image.open(filename)
        img.close()
        return True
    except (IOError, SyntaxError):
        return False
option=True
if len(sys.argv) != 2:
    print("Usage: python script.py <imgPath>")
    c=input(f"return...{sys.argv[1]}")
    sys.exit(1)
imgPath = sys.argv[1]
imgName = os.path.basename(imgPath)
if isImg(imgName):
    print(f"Selected File {imgName}")
    image = Image.open(imgPath)
    image = image.convert('RGB')
    while(option):
    	frmat = int(input("Enter\n1.Jpg or 2.PNG\nOption: "))
    	if frmat == 1:
    		option=False
    		rename = input("Enter new File Name...\nLeave empty to let the original name\nNew Name: ")
    		if rename != "":
    			image.save(f"{rename}.jpg")
    			c=input(f"File Saved as {rename}.jpg...")
    		else:
    			image.save(f"{imgName.split(".")[0]}.jpg")
    			c=input(f"File Saved as {imgName.split(".")[0]}.jpg...")
    	elif frmat == 2:
    		option=False
    		rename = input("Enter new File Name...\nLeave empty to let the original name\nNew Name: ")
    		if rename != "":
    			image.save(f"{rename.split(".")[0]}.png")
    			c=input(f"File Saved as {rename}.png...")
    		else:
    			image.save(f"{imgName.split(".")[0]}.png")
    			c=input(f"File Saved as {imgName.split(".")[0]}.png...")
    	else:
    		print("Selected option doesn't exist")
else:
    c=input(f"{imgName} is not an Image")