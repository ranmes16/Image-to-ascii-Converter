from PIL import Image
import numpy as np

# loading the image
image_path = './image.jpg'
image = Image.open(image_path)

# resizing the image
new_width = 100
aspect_ratio = image.size[1] / image.size[0]
new_height = int(aspect_ratio * new_width * 0.6) 
image = image.resize((new_width, new_height))


# getting the gray scale
gray_image = image.convert('L')

pixel_array = np.array(gray_image)

pixel_array = (pixel_array / 255.0) * 1000

width, height = image.size


# printing the ascii character based on the grayscale of the picture 
for y in range(height):
    for x in range(width):
        if pixel_array[y][x] == 0:
            print(" ", end="")
        elif pixel_array[y][x] <= 100:
            print(".", end="")
        elif pixel_array[y][x] <= 200:
            print(":", end="")
        elif pixel_array[y][x] <= 300:
            print("-", end="")
        elif pixel_array[y][x] <= 400:
            print("=", end="")
        elif pixel_array[y][x] <= 500:
            print("+", end="")
        elif pixel_array[y][x] <= 600:
            print("*", end="")
        elif pixel_array[y][x] <= 700:
            print("#", end="")
        elif pixel_array[y][x] <= 800:
            print("%", end="")
        elif pixel_array[y][x] <= 900:
            print("&", end="")
        elif pixel_array[y][x] <= 1000:
            print("@", end="")
    print()
