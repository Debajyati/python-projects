import os
import sys
from PIL import Image

# Grab first and second argument
image_Folder: str = "./" + sys.argv[1]
output_Folder: str = "./" + sys.argv[2]

  # Check if 'new/' exists as a directory
  # if not create that first

if os.path.isdir(output_Folder):
    pass
else:
    os.mkdir(output_Folder)


def convert() -> None:
    i = 1
    for img in os.listdir(image_Folder):
        finalFile = Image.open(f"{image_Folder}{img}")
        namE: str = f"IMG{i}.png"
        i += 1
        finalFile.save(f"{output_Folder}{namE}", "png")
        print(f"<{img}>==><{namE}>--Convertion done!")
    """
    Loop through the `image_Folder`,
    convert images to png format,
    save them to the `output_Folder` folder
    """


convert()

