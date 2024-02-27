import sys
import os
from PIL import Image
import pillow_avif

if len(sys.argv) != 2:
    print("Usage: python script.py <imgPath>")
    c=input(f"return...{sys.argv[1]}")
    sys.exit(1)
imgPath = sys.argv[1]
imgName = os.path.basename(imgPath)

print(f"Selected File {imgName}")
image = Image.open(imgPath)
image = image.convert('RGB')

image.save(f"{imgName.split(".")[0]}.jpg")