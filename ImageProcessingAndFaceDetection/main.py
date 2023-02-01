import cv2 as cv
import PIL
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL import ImageFilter


#load the images
img = Image.open('path/to/index.jpeg')
img1 = Image.open('path/to/index1.jpeg')

print('''
1. Display images
2. Rotate one of the images
3. Apply 2 different filters on both images and display them
4. Create a new image containing the 2 images
5. Crop an object from one of the images and show
6. Draw a rectangle around the cropped element above
7. Add to the images my name, dimenstion of font = my birthday, R = 255, G = 13, B = 12
8. Create a contact sheet of images with 12 images per row
9. Exit
''')


while 1:
      n = int(input('Your choice: '))
      #display images and save one of them with a different extension
      if n == 1:
            img.show()
            img1.show()

      #save one of the images with a different extension
      try:
            img.save(r'/home/andrei/Desktop/IA/13Dec/images/index.png')
      except FileExistsError():
            print('File already exists')

      #rotate one of the images
      if n == 2:
            img1 = img1.rotate(90)
            img1.show()

      #apply 2 different filters on both images and display them
      if n == 3:
            img = img.convert('RGB')
            blurred = img.filter(PIL.ImageFilter.BLUR)
            blurred.show()
            blurred = img.filter(PIL.ImageFilter.EMBOSS)
            blurred.show()

            img1 = img1.convert('RGB')
            blurred1 = img1.filter(PIL.ImageFilter.BLUR)
            blurred1.show()
            blurred1 = img1.filter(PIL.ImageFilter.EMBOSS)
            blurred1.show()

      #create a new image containing the 2 images
      if n == 4:
            new_img = Image.new('RGB', (img.width + img1.width, img.height))
            new_img.paste(img, (0, 0))
            new_img.paste(img1, (img.width, 0))
            new_img.show()

      #crop an object from one of the images and show
      if n == 5:
            cropped = img.crop((2, 2, 100, 100))
            cropped.show()

      #draw a rectangle around the cropped element above
      if n == 6:
            draw = ImageDraw.Draw(img)
            draw.rectangle(((2, 2), (100, 100)), outline='blue')
            img.show()

      #add to the images my name, dimenstion of font = my birthday, R = 255, G = 13, B = 12
      if n == 7:
            draw = ImageDraw.Draw(img)
            text = "Panait Andrei-Stefan"
            font = ImageFont.truetype(r'/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 17)
            draw.text((0, 0), text, (255, 13, 1200), font=font)
            img.show()

      #create a contact sheet of images with 3 images per row
      if n == 8:
            enhancer=ImageEnhance.Sharpness(img)
            images=[]
            for i in range(1, 13):
                  images.append(enhancer.enhance(i/13))
            first_image = images[0]
            contact_sheet = PIL.Image.new(first_image.mode, (img.width * 4, img.height * 4))
            x = 0
            y = 0
            for i in images:
                  contact_sheet.paste(img, (x, y))
                  if x + img.width == contact_sheet.width:
                        x = 0
                        y = y + img.height
                  else:
                        x = x + img.width
            contact_sheet.show()

      if n == 9:
            break
