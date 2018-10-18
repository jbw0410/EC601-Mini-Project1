import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Instantiates a client
client = vision.ImageAnnotatorClient()
for i in range(1,16):
# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__),'%d.jpg'%(i))

# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('image%dlabels:'%i)
	for label in labels:
		print(label.description)
#		print(label.score)


	font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)

	im1=Image.open(file_name)


	draw=ImageDraw.Draw(im1)

	j=0

	for label in labels:

		draw.text((0,j),label.description,(255,255,0),font=font)

		j+=30
	
	draw=ImageDraw.Draw(im1)

	im1.save("%d.jpg"%(i))
