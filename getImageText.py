import easyocr
import sys
import Image


def readTextFromImage(img_path):
    img_reader = easyocr.Reader(["en"])
    img_parts = img_reader.readtext(img_path)
    img_text = ""
    for parts in img_parts:
        text = ""
        try:
            texts = [text + part for part in parts if isinstance(part, str)]
            if len(texts) > 0:
                for text in texts:
                    img_text += text
        except:
            print("error")
    return img_text


def cropImageBottomCorner(logo_path):
    # Load the original image
    image = Image.open(main_image)

    # Get the width and height of the original image
    width, height = image.size

    # Define the dimensions of the cropped portion (220px x 45px)
    crop_width = 100
    crop_height = 20

    # Calculate the coordinates for the bottom right corner
    x1 = width - crop_width
    y1 = height - crop_height
    x2 = width
    y2 = height

    # Crop the image
    cropped_image = image.crop((x1, y1, x2, y2)).resize((220, 45))
    cropped_image.save(logo_path)  # You can change the file format if needed


def cropImageTopLeftCorner():
    # Load the original image
    image = Image.open(main_image)

    # Get the width and height of the original image
    width, height = image.size

    # Define the dimensions of the cropped portion (220px x 45px)
    crop_width = width
    crop_height = 40

    # Calculate the coordinates for the bottom right corner
    x1 = 0
    y1 = crop_height
    x2 = width
    y2 = height

    cropped_image = image.crop((x1, y1, x2, y2))

    # Save the cropped and resized image
    cropped_image.save(main_image)  # You can change the file format if needed


def isVariableNotEmptyString(text):
    return isinstance(text, str) and len(text) > 0


img_name = sys.argv[1]
crop = sys.argv[2]
main_image = f"D:\\cars data\\images\\trim\\{img_name}.jpg"
logo = "D:\\cars data\\images\\trim\\logo.jpg"
label = "D:\\cars data\\images\\trim\\label.jpg"

try:
    if crop == "true":
        cropImageTopLeftCorner()
        img_text = readTextFromImage(main_image).lower()
        check = isVariableNotEmptyString(img_text)
        sys.stdout.write(str(check).lower())
        sys.stdout.flush()
        sys.exit()

    img_text = readTextFromImage(main_image).lower()
    isAutoDataFound = isVariableNotEmptyString(img_text)

    if not isAutoDataFound:
        cropImageBottomCorner(logo)
        img_text = readTextFromImage(logo)
        isAutoDataFound = isVariableNotEmptyString(img_text)

    # Send the output back to Node.js
    sys.stdout.write(str(isAutoDataFound).lower())
    sys.stdout.flush()
    sys.exit()

except:
    sys.stdout.flush()
    sys.exit()
