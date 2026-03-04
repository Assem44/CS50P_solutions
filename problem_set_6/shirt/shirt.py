import sys, os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]

input_img_name = sys.argv[1]
output_img_name = sys.argv[2]

input_extension = os.path.splitext(input_img_name)[1].lower()
output_extension = os.path.splitext(output_img_name)[1].lower()

if not input_extension in valid_extensions:
    sys.exit("Invalid input")
elif not output_extension in valid_extensions:
    sys.exit("Invalid output")
elif not input_extension == output_extension:
    sys.exit("Input and output have different extensions")

try:

    shirt_img = Image.open("shirt.png")
    shirt_img_size = shirt_img.size

    with Image.open(input_img_name) as img:

        output_photo = ImageOps.fit(img, shirt_img_size)
        output_photo.paste(shirt_img, shirt_img)

        output_photo.save(output_img_name)

except FileNotFoundError:
    sys.exit("Input does not exist")
