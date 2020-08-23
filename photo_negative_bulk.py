########################################
# How to use
# Install the required libraries i.e PIL
# Create a new folder in your pc and store those photos which you need to convert to photo negative
# Create another folder leave it empty (to store the processed photos)
# You will be asked to enter the location of the folder where photos are stored and where processed photos need to be stored
# enter it in this format -> C:/Users/Shehzad/Desktop/A level Physics/class08 [SEE TO FORWARD SLASH]
# Thanks

##########################################


# import

from PIL import Image
from PIL import ImageFilter
import os


# Function to convert normal photos to negative

def to_negative(img,save_path,file_name):

    print("editing file " + file_name + "...")
    # Read pixels and apply negative transformation

    for i in range(0, img.size[0]-1):

        for j in range(0, img.size[1]-1):

            # Get pixel value at (x,y) position of the image

            pixelColorVals = img.getpixel((i,j))

        

            # Invert color

            redPixel    = 255 - pixelColorVals[0] # Negate red pixel

            greenPixel  = 255 - pixelColorVals[1] # Negate green pixel

            bluePixel   = 255 - pixelColorVals[2] # Negate blue pixel

                    

            # Modify the image with the inverted pixel values

            img.putpixel((i,j),(redPixel, greenPixel, bluePixel))


    # Saves the negative photo
    print("saving file " + file_name + "...")
    img.save(save_path + "/" + file_name)
    print(file_name + " saved.")

# Main Program


# Gets path of the photo folder and sets it to current directory
path = input("Enter the path where all your photos are stored (e.g C:/Users/Shehzad/Desktop/A level Physics/class08): ")
save_path = input("Enter the path to store your photo negative photos(e.g C:/Users/Shehzad/Desktop/A level Physics/class08neg): ")
os.chdir(path)

files_list = os.listdir()
print("\ngetting files...\n")

count = 0
for i in files_list:
    print("opening file " + i + "...")
    img = Image.open(i)
    to_negative(img,save_path,i)
    count += 1
    print("\nProgress " + str(count) + " / " + str(len(files_list)) + "...\n")

print("Task Completed")



